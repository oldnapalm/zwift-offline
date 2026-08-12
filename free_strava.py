import os
import re
import time
import uuid
from io import BytesIO
from html import unescape
from requests import Session
from requests_toolbelt.multipart.encoder import MultipartEncoder

UPLOAD_URL = "https://www.strava.com/upload/files"
SELECT_URL = "https://www.strava.com/upload/select"
PROGRESS_URL = "https://www.strava.com/upload/progress.json"
BULK_UPDATE_URL = "https://www.strava.com/athlete/training_activities/bulk_update"
PHOTO_METADATA_URL = "https://www.strava.com/photos/metadata"
EDIT_URL = "https://www.strava.com/activities/%s/edit"
ACTIVITY_URL = "https://www.strava.com/activities/%s"
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


def new_session(cookie):
    s = Session()
    s.headers["User-Agent"] = USER_AGENT
    s.cookies.set("_strava4_session", cookie, domain=".strava.com", path="/")
    return s


def check_session(cookie):
    return "Upload and Sync Your Activities" in new_session(cookie).get(SELECT_URL).text


def parse_form(form):
    data = {}
    for m in re.finditer(r"<input\b[^>]*>", form):
        tag = m.group(0)
        if re.search(r"\bdisabled\b|\btype=[\"'](?:submit|button|file)[\"']", tag):
            continue
        name = re.search(r'name="([^"]+)"', tag)
        if not name:
            continue
        name = unescape(name.group(1))
        val = re.search(r'value="([^"]*)"', tag)
        val = unescape(val.group(1)) if val else ""
        if re.search(r'type="checkbox"', tag):
            if re.search(r"\bchecked\b", tag):
                data[name] = val or "1"
        else:
            data[name] = val
    for m in re.finditer(r"<select\b[^>]*>.*?</select>", form, re.S):
        tag = m.group(0)
        if re.search(r"\bdisabled\b", tag):
            continue
        name = re.search(r'name="([^"]+)"', tag)
        if not name:
            continue
        opts = re.findall(r"<option\b([^>]*)>([^<]*)</option>", tag)
        if not opts:
            continue
        sel = [v for a, v in opts if "selected" in a]
        data[unescape(name.group(1))] = unescape((sel or [opts[0][1]])[0])
    for m in re.finditer(r"<textarea\b[^>]*>.*?</textarea>", form, re.S):
        tag = m.group(0)
        name = re.search(r'name="([^"]+)"', tag)
        if not name:
            continue
        val = re.search(r">(.*)</textarea>", tag, re.S)
        data[unescape(name.group(1))] = unescape(val.group(1)) if val else ""
    return data


def attach_photos(s, aid, photos):
    edit = s.get(EDIT_URL % aid)
    if not edit.ok:
        raise RuntimeError("Unable to get activity edit page")
    m = re.search(r'name="authenticity_token" value="([^"]+)"', edit.text)
    if not m:
        raise RuntimeError("Cannot find authenticity token on edit page")
    token = unescape(m.group(1))
    m = re.search(r"var athleteId = (\d+);", edit.text)
    if not m:
        raise RuntimeError("Cannot find athlete id on edit page")
    athlete_id = int(m.group(1))
    m = re.search(r'<form class="edit_activity".*?</form>', edit.text, re.S)
    if not m:
        raise RuntimeError("Cannot find edit form on edit page")
    data = parse_form(m.group(0))
    count = 0
    for photo in photos:
        uid = str(uuid.uuid4())
        taken_at = int(os.path.getmtime(photo) * 1000)
        r = s.put(
            PHOTO_METADATA_URL,
            data={"athlete_id": athlete_id, "uuid": uid, "taken_at": taken_at},
            headers={"X-CSRF-Token": token},
        )
        if not r.ok:
            raise RuntimeError("Photo metadata failed: %s" % photo)
        meta = r.json()
        with open(photo, "rb") as f:
            raw = f.read()
        r = s.put(meta["uri"], data=raw, headers=meta["header"])
        if not r.ok:
            raise RuntimeError("Photo upload failed: %s" % photo)
        data["photos[%s][caption]" % uid] = ""
        data["photos[%s][rank]" % uid] = str(count)
        data["photos[%s][media_type]" % uid] = "1"
        count += 1
    if not count:
        return
    r = s.post(ACTIVITY_URL % aid, data=data)
    if not r.ok:
        raise RuntimeError("Failed to save photos on activity: %s" % r.text[:200])


def upload_activity(cookie, filename, fit, name, photos=()):
    s = new_session(cookie)

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
        if photos:
            attach_photos(s, aid, photos)
