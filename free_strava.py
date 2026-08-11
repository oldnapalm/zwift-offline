import re
import time
from io import BytesIO
from html import unescape
from requests import Session
from requests_toolbelt.multipart.encoder import MultipartEncoder

UPLOAD_URL = "https://www.strava.com/upload/files"
SELECT_URL = "https://www.strava.com/upload/select"
PROGRESS_URL = "https://www.strava.com/upload/progress.json"
BULK_UPDATE_URL = "https://www.strava.com/athlete/training_activities/bulk_update"
SPORT_TYPE = "VirtualRide"
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
)


def wait_ready(s, upload_id):
    for _ in range(60):
        item = s.get(PROGRESS_URL, params={"ids[]": upload_id}).json()[0]
        if item.get("workflow") == "success":
            return item
        if item.get("workflow") in ("error", "empty"):
            raise RuntimeError("Upload failed: %s" % item.get("workflow"))
        time.sleep(1)
    raise RuntimeError("Upload timed out")


def rename(s, act, aid, name, sport_type, token):
    data = {"id": aid, "name": name}
    for key in (
        "description",
        "commute",
        "trainer",
        "workout_type",
        "bike_id",
        "athlete_gear_id",
    ):
        if key in act:
            data[key] = act[key]
    data["sport_type"] = sport_type or act.get("type")
    r = s.post(
        BULK_UPDATE_URL, json={"activities": [data]}, headers={"X-CSRF-Token": token}
    )
    if r.ok:
        return
    if sport_type and sport_type != "Ride":
        rename(s, act, aid, name, "Ride", token)
    else:
        raise RuntimeError("Failed to set name: %s" % r.text)


def upload_activity(cookie, filename, fit, name):
    s = Session()
    s.headers["User-Agent"] = USER_AGENT
    s.cookies.set("_strava4_session", cookie, domain=".strava.com", path="/")

    response = s.get(SELECT_URL)
    if "Upload and Sync Your Activities" not in response.text:
        raise RuntimeError("Invalid Strava session")

    m = re.search(r'<meta name="csrf-token" content="([^"]+)"', response.text)
    if not m:
        m = re.search(r'name="authenticity_token" value="([^"]+)"', response.text)
    if not m:
        raise RuntimeError("Cannot find authenticity token on upload page")
    token = unescape(m.group(1))

    mp_encoder = MultipartEncoder(
        fields={
            "_method": "post",
            "authenticity_token": token,
            "files[]": (filename, BytesIO(fit), "application/octet-stream"),
        }
    )
    response = s.post(
        UPLOAD_URL,
        data=mp_encoder,
        headers={"Content-Type": mp_encoder.content_type},
    )
    if "workflow" not in response.text:
        raise RuntimeError(response.text)

    for upload in response.json():
        item = wait_ready(s, upload.get("id"))
        act = item.get("activity") or item
        aid = act.get("id")
        if not aid:
            raise RuntimeError("No activity id in upload response")
        rename(s, act, aid, name, SPORT_TYPE, token)
