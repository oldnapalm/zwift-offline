# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rprofile.proto\"\xff\x1d\n\rPlayerProfile\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x14\n\x0cserver_realm\x18\x02 \x01(\x03\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x12\n\nfirst_name\x18\x04 \x01(\t\x12\x11\n\tlast_name\x18\x05 \x01(\t\x12\x0f\n\x07is_male\x18\x06 \x01(\x08\x12\n\n\x02\x66\x37\x18\x07 \x01(\t\x12\x17\n\x0fweight_in_grams\x18\t \x01(\r\x12\x0b\n\x03\x66tp\x18\n \x01(\r\x12\x0b\n\x03\x66\x31\x31\x18\x0b \x01(\r\x12\x11\n\tbody_type\x18\x0c \x01(\r\x12\x11\n\thair_type\x18\r \x01(\r\x12\x18\n\x10\x66\x61\x63ial_hair_type\x18\x0e \x01(\r\x12\x18\n\x10ride_helmet_type\x18\x0f \x01(\r\x12\x14\n\x0cglasses_type\x18\x10 \x01(\r\x12\x17\n\x0fride_shoes_type\x18\x11 \x01(\r\x12\x17\n\x0fride_socks_type\x18\x12 \x01(\r\x12\x13\n\x0bride_gloves\x18\x13 \x01(\r\x12\x13\n\x0bride_jersey\x18\x14 \x01(\x07\x12\x0b\n\x03\x66\x32\x31\x18\x15 \x01(\x07\x12\x18\n\x10\x62ike_wheel_front\x18\x16 \x01(\x07\x12\x17\n\x0f\x62ike_wheel_rear\x18\x17 \x01(\x07\x12\x12\n\nbike_frame\x18\x18 \x01(\x07\x12\x0b\n\x03\x66\x32\x35\x18\x19 \x01(\x07\x12\x0b\n\x03\x66\x32\x36\x18\x1a \x01(\x07\x12\x19\n\x11\x62ike_frame_colour\x18\x1b \x01(\x06\x12\x0b\n\x03\x66\x32\x38\x18\x1c \x01(\x06\x12\x0b\n\x03\x66\x32\x39\x18\x1d \x01(\x06\x12\x0b\n\x03\x66\x33\x30\x18\x1e \x01(\x06\x12\x0b\n\x03\x66\x33\x31\x18\x1f \x01(\x06\x12\x0b\n\x03\x66\x33\x32\x18  \x01(\x06\x12\x12\n\nsaved_game\x18! \x01(\x0c\x12\x14\n\x0c\x63ountry_code\x18\" \x01(\r\x12 \n\x18total_distance_in_meters\x18# \x01(\r\x12 \n\x18\x65levation_gain_in_meters\x18$ \x01(\r\x12\x1e\n\x16time_ridden_in_minutes\x18% \x01(\r\x12\x1b\n\x13total_in_kom_jersey\x18& \x01(\r\x12!\n\x19total_in_sprinters_jersey\x18\' \x01(\r\x12\x1e\n\x16total_in_orange_jersey\x18( \x01(\r\x12\x18\n\x10total_watt_hours\x18) \x01(\r\x12\x1d\n\x15height_in_millimeters\x18* \x01(\r\x12\x0b\n\x03\x64ob\x18+ \x01(\t\x12\x16\n\x0emax_heart_rate\x18, \x01(\r\x12\x1b\n\x13\x63onnected_to_strava\x18- \x01(\x08\x12\x10\n\x08total_xp\x18. \x01(\r\x12\x18\n\x10total_gold_drops\x18/ \x01(\r\x12 \n\x0bplayer_type\x18\x30 \x01(\x0e\x32\x0b.PlayerType\x12\x19\n\x11\x61\x63hievement_level\x18\x31 \x01(\r\x12\x12\n\nuse_metric\x18\x32 \x01(\x08\x12\x16\n\x0estrava_premium\x18\x33 \x01(\x08\x12&\n\x12power_source_model\x18\x34 \x01(\x0e\x32\n.PowerType\x12\x0b\n\x03\x66\x35\x33\x18\x35 \x01(\r\x12\x0b\n\x03\x66\x35\x34\x18\x36 \x01(\r\x12\x0b\n\x03\x61ge\x18\x37 \x01(\r\x12\x0b\n\x03\x66\x35\x36\x18\x38 \x01(\x07\x12\x0b\n\x03\x66\x35\x37\x18\x39 \x01(\r\x12\x18\n\x10large_avatar_url\x18: \x01(\t\x12\x14\n\x0cprivacy_bits\x18; \x01(\x06\x12)\n\x0c\x65ntitlements\x18< \x03(\x0b\x32\x13.ProfileEntitlement\x12\x30\n\x0csocial_facts\x18= \x01(\x0b\x32\x1a.PlayerProfile.SocialFacts\x12$\n\rfollow_status\x18> \x01(\x0e\x32\r.FollowStatus\x12#\n\x1b\x63onnected_to_training_peaks\x18? \x01(\x08\x12 \n\x18\x63onnected_to_todays_plan\x18@ \x01(\x08\x12\x38\n\x10\x65nrolled_program\x18\x41 \x01(\x0e\x32\x1e.PlayerProfile.EnrolledProgram\x12\x15\n\rtodayplan_url\x18\x42 \x01(\t\x12\x0b\n\x03\x66\x36\x37\x18\x43 \x01(\r\x12\x16\n\x0erun_shirt_type\x18\x44 \x01(\x07\x12\x17\n\x0frun_shorts_type\x18\x45 \x01(\x07\x12\x16\n\x0erun_shoes_type\x18\x46 \x01(\x07\x12\x16\n\x0erun_socks_type\x18G \x01(\x07\x12\x17\n\x0frun_helmet_type\x18H \x01(\x07\x12\x19\n\x11run_arm_accessory\x18I \x01(\x07\x12\x1a\n\x12total_run_distance\x18J \x01(\r\x12#\n\x1btotal_run_experience_points\x18K \x01(\r\x12\x0b\n\x03\x66\x37\x36\x18L \x01(\x07\x12\x0b\n\x03\x66\x37\x37\x18M \x01(\x07\x12\x0b\n\x03\x66\x37\x38\x18N \x01(\x07\x12\x0b\n\x03\x66\x37\x39\x18O \x01(\x07\x12\x0b\n\x03\x66\x38\x30\x18P \x01(\r\x12\x0b\n\x03\x66\x38\x31\x18Q \x01(\r\x12#\n\x0csubscription\x18R \x01(\x0b\x32\r.Subscription\x12\x1d\n\x15mix_panel_distinct_id\x18S \x01(\t\x12\x1d\n\x15run_achievement_level\x18T \x01(\r\x12!\n\x19total_run_time_in_minutes\x18U \x01(\r\x12\x15\n\x05sport\x18V \x01(\x0e\x32\x06.Sport\x12\x1d\n\x15utc_offset_in_minutes\x18W \x01(\r\x12!\n\x19\x63onnected_to_under_armour\x18X \x01(\x08\x12\x1a\n\x12preferred_language\x18Y \x01(\t\x12\x13\n\x0bhair_colour\x18Z \x01(\r\x12\x1a\n\x12\x66\x61\x63ial_hair_colour\x18[ \x01(\r\x12\x0b\n\x03\x66\x39\x32\x18\\ \x01(\r\x12\x0b\n\x03\x66\x39\x33\x18] \x01(\r\x12\x19\n\x11run_shorts_length\x18^ \x01(\r\x12\x0b\n\x03\x66\x39\x35\x18_ \x01(\r\x12\x18\n\x10run_socks_length\x18` \x01(\r\x12\x0b\n\x03\x66\x39\x37\x18\x61 \x01(\r\x12\x19\n\x11ride_socks_length\x18\x62 \x01(\r\x12\x0b\n\x03\x66\x39\x39\x18\x63 \x01(\r\x12\x0c\n\x04\x66\x31\x30\x30\x18\x64 \x01(\r\x12\x0c\n\x04\x66\x31\x30\x31\x18\x65 \x01(\r\x12\x0c\n\x04\x66\x31\x30\x32\x18\x66 \x01(\r\x12\x0c\n\x04\x66\x31\x30\x33\x18g \x01(\r\x12\x0c\n\x04\x66\x31\x30\x34\x18h \x01(\r\x12\x1d\n\x15\x63onnected_to_withings\x18i \x01(\x08\x12\x1b\n\x13\x63onnected_to_fitbit\x18j \x01(\x08\x12\x1c\n\x14launched_game_client\x18l \x01(\t\x12\x1b\n\x13\x63urrent_activity_id\x18m \x01(\x03\x12\x1b\n\x13\x63onnected_to_garmin\x18n \x01(\x08\x12*\n\treminders\x18o \x03(\x0b\x32\x17.PlayerProfile.Reminder\x12\x0c\n\x04\x66\x31\x31\x32\x18p \x01(\x08\x12&\n\x12private_attributes\x18q \x03(\x0b\x32\n.Attribute\x12%\n\x11public_attributes\x18r \x03(\x0b\x32\n.Attribute\x12\x1a\n\x12total_run_calories\x18s \x01(\x05\x12\x0c\n\x04\x66\x31\x31\x36\x18t \x01(\x03\x12\x1f\n\x17run_time_1mi_in_seconds\x18u \x01(\x05\x12\x1f\n\x17run_time_5km_in_seconds\x18v \x01(\x05\x12 \n\x18run_time_10km_in_seconds\x18w \x01(\x05\x12)\n!run_time_half_marathon_in_seconds\x18x \x01(\x05\x12)\n!run_time_full_marathon_in_seconds\x18y \x01(\x05\x12\x0c\n\x04\x66\x31\x32\x32\x18z \x01(\x05\x12@\n\x14\x63ycling_organization\x18{ \x01(\x0e\x32\".PlayerProfile.CyclingOrganization\x12\x0c\n\x04\x66\x31\x32\x34\x18| \x01(\t\x12\x36\n\x18\x64\x65\x66\x61ult_activity_privacy\x18} \x01(\x0e\x32\x14.ActivityPrivacyType\x12\x1e\n\x16\x63onnected_to_runtastic\x18~ \x01(\x08\x12)\n\x10property_changes\x18\x7f \x03(\x0b\x32\x0f.PropertyChange\x12\x13\n\ncur_streak\x18\x83\x01 \x01(\r\x12\x13\n\nmax_streak\x18\x84\x01 \x01(\r\x1a\xa7\x02\n\x0bSocialFacts\x12\x12\n\nprofile_id\x18\x01 \x01(\x03\x12\x17\n\x0f\x66ollowers_count\x18\x02 \x01(\x05\x12\x17\n\x0f\x66ollowees_count\x18\x03 \x01(\x05\x12\x31\n)followees_in_common_with_logged_in_player\x18\x04 \x01(\x05\x12:\n#follower_status_of_logged_in_player\x18\x05 \x01(\x0e\x32\r.FollowStatus\x12:\n#followee_status_of_logged_in_player\x18\x06 \x01(\x0e\x32\r.FollowStatus\x12\'\n\x1fis_favorite_of_logged_in_player\x18\x07 \x01(\x08\x1a\x9c\x01\n\x08Reminder\x12\n\n\x02\x66\x31\x18\x01 \x01(\x03\x12\n\n\x02\x66\x32\x18\x02 \x01(\t\x12\n\n\x02\x66\x33\x18\x03 \x01(\x03\x12\x34\n\x02\x66\x34\x18\x04 \x03(\x0b\x32(.PlayerProfile.Reminder.ReminderProperty\x1a\x36\n\x10ReminderProperty\x12\n\n\x02\x66\x31\x18\x01 \x01(\x03\x12\n\n\x02\x66\x32\x18\x02 \x01(\t\x12\n\n\x02\x66\x33\x18\x03 \x01(\t\"|\n\x0f\x45nrolledProgram\x12\x14\n\x10\x45NROLLEDPROGRAM0\x10\x00\x12\x11\n\rZWIFT_ACADEMY\x10\x01\x12\x14\n\x10\x45NROLLEDPROGRAM2\x10\x02\x12\x14\n\x10\x45NROLLEDPROGRAM3\x10\x03\x12\x14\n\x10\x45NROLLEDPROGRAM4\x10\x04\"w\n\x13\x43yclingOrganization\x12\x16\n\x12NO_CYCLING_LICENSE\x10\x00\x12\x18\n\x14\x43YCLING_SOUTH_AFRICA\x10\x01\x12\x15\n\x11\x43YCLING_AUSTRALIA\x10\x02\x12\x17\n\x13\x43YCLING_NEW_ZEALAND\x10\x03\"2\n\x0ePlayerProfiles\x12 \n\x08profiles\x18\x01 \x03(\x0b\x32\x0e.PlayerProfile\"\xb0\x06\n\x12ProfileEntitlement\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32#.ProfileEntitlement.EntitlementType\x12\n\n\x02id\x18\x02 \x01(\x03\x12<\n\x06status\x18\x03 \x01(\x0e\x32,.ProfileEntitlement.ProfileEntitlementStatus\x12\x0e\n\x06period\x18\x04 \x01(\t\x12\x17\n\x0f\x62\x65gin_time_unix\x18\x05 \x01(\r\x12\x15\n\rend_time_unix\x18\x06 \x01(\r\x12\x12\n\nkilometers\x18\x07 \x01(\r\x12\x1c\n\x14\x62\x65gin_total_distance\x18\x08 \x01(\r\x12\x1a\n\x12\x65nd_total_distance\x18\t \x01(\r\x12\x0e\n\x06source\x18\n \x01(\t\x12.\n\x08platform\x18\x0b \x01(\x0e\x32\x1c.ProfileEntitlement.Platform\x12\x19\n\x11renewal_date_unix\x18\x0c \x01(\r\x12\x18\n\x10new_trial_system\x18\r \x01(\x08\x12/\n\tplatforms\x18\x0e \x03(\x0e\x32\x1c.ProfileEntitlement.Platform\"L\n\x0f\x45ntitlementType\x12\x14\n\x10\x45NTITLEMENTTYPE0\x10\x00\x12\x08\n\x04RIDE\x10\x01\x12\x07\n\x03RUN\x10\x02\x12\x07\n\x03ROW\x10\x03\x12\x07\n\x03USE\x10\x04\"\x91\x01\n\x18ProfileEntitlementStatus\x12\x16\n\x12\x45NTITLEMENTSTATUS0\x10\x00\x12\x0b\n\x07\x45XPIRED\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\x12\x0c\n\x08INACTIVE\x10\x04\x12(\n$APPLIED_AS_SUBSCRIPTION_TRIAL_PERIOD\x10\x05\"\x86\x01\n\x08Platform\x12\x10\n\x0cPLATFORM_OSX\x10\x00\x12\x0f\n\x0bPLATFORM_PC\x10\x01\x12\x10\n\x0cPLATFORM_IOS\x10\x02\x12\x14\n\x10PLATFORM_ANDROID\x10\x03\x12\x11\n\rPLATFORM_TVOS\x10\x04\x12\r\n\tPLATFORM5\x10\x05\x12\r\n\tPLATFORM6\x10\x06\"@\n\x13ProfileEntitlements\x12)\n\x0c\x65ntitlements\x18\x01 \x03(\x0b\x32\x13.ProfileEntitlement\"\xcc\x02\n\x0cSubscription\x12&\n\x07gateway\x18\x01 \x01(\x0e\x32\x15.Subscription.Gateway\x12\x30\n\x06status\x18\x02 \x01(\x0e\x32 .Subscription.SubscriptionStatus\"#\n\x07Gateway\x12\r\n\tBRAINTREE\x10\x00\x12\t\n\x05\x41PPLE\x10\x01\"\xbc\x01\n\x12SubscriptionStatus\x12\x07\n\x03NEW\x10\x00\x12\x0b\n\x07\x45XPIRED\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\x12\x0c\n\x08PAST_DUE\x10\x04\x12\x0b\n\x07PENDING\x10\x05\x12\x0c\n\x08SUBERROR\x10\x06\x12\x10\n\x0cUNRECOGNIZED\x10\x07\x12\x0b\n\x07UNKNOWN\x10\x08\x12\x1f\n\x1b\x41\x43TIVE_WITH_PAYMENT_FAILURE\x10\t\x12\r\n\tABANDONED\x10\n\"\x96\x01\n\x0ePropertyChange\x12)\n\rproperty_name\x18\x01 \x02(\x0e\x32\x12.PropertyChange.Id\x12\x14\n\x0c\x63hange_count\x18\x02 \x01(\x05\x12\x13\n\x0bmax_changes\x18\x03 \x01(\x05\".\n\x02Id\x12\t\n\x05TYPE0\x10\x00\x12\x11\n\rDATE_OF_BIRTH\x10\x01\x12\n\n\x06GENDER\x10\x02\"X\n\tAttribute\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x14\n\x0cnumber_value\x18\x02 \x01(\x03\x12\x13\n\x0b\x66loat_value\x18\x03 \x01(\x02\x12\x14\n\x0cstring_value\x18\x05 \x01(\t\"\x1e\n\x10\x41\x63hievementEntry\x12\n\n\x02id\x18\x01 \x02(\x05\"7\n\x0c\x41\x63hievements\x12\'\n\x0c\x61\x63hievements\x18\x01 \x03(\x0b\x32\x11.AchievementEntry\"6\n\x12\x42\x65stEffortPointMsg\x12\r\n\x05power\x18\x01 \x02(\x01\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\"\x9b\x02\n\x18PowerCurveAggregationMsg\x12\x33\n\x05watts\x18\x01 \x03(\x0b\x32$.PowerCurveAggregationMsg.WattsEntry\x12?\n\x0cwatts_per_kg\x18\x02 \x03(\x0b\x32).PowerCurveAggregationMsg.WattsPerKgEntry\x1a\x41\n\nWattsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.BestEffortPointMsg:\x02\x38\x01\x1a\x46\n\x0fWattsPerKgEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.BestEffortPointMsg:\x02\x38\x01*;\n\x13\x41\x63tivityPrivacyType\x12\n\n\x06PUBLIC\x10\x00\x12\x0b\n\x07PRIVATE\x10\x01\x12\x0b\n\x07\x46RIENDS\x10\x02*E\n\x05Sport\x12\x0b\n\x07\x43YCLING\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\n\n\x06ROWING\x10\x02\x12\n\n\x06SPORT3\x10\x03\x12\n\n\x06SPORT4\x10\x04*\x9f\x01\n\nPlayerType\x12\x0f\n\x0bPLAYERTYPE0\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x0f\n\x0bPRO_CYCLIST\x10\x02\x12\x0f\n\x0bZWIFT_STAFF\x10\x03\x12\x0e\n\nAMBASSADOR\x10\x04\x12\x0c\n\x08VERIFIED\x10\x05\x12\x07\n\x03ZED\x10\x06\x12\x07\n\x03ZAC\x10\x07\x12\x12\n\x0ePRO_TRIATHLETE\x10\x08\x12\x0e\n\nPRO_RUNNER\x10\t*B\n\tPowerType\x12\x17\n\nPT_UNKNOWN\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0e\n\nPT_VIRTUAL\x10\x00\x12\x0c\n\x08PT_METER\x10\x01*\x9e\x01\n\x0c\x46ollowStatus\x12\x11\n\rFOLLOWSTATUS0\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x16\n\x12REQUESTS_TO_FOLLOW\x10\x02\x12\x10\n\x0cIS_FOLLOWING\x10\x03\x12\x15\n\x11HAS_BEEN_DECLINED\x10\x07\x12\x0e\n\nIS_BLOCKED\x10\x04\x12\x13\n\x0fNO_RELATIONSHIP\x10\x05\x12\x08\n\x04SELF\x10\x06')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'profile_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POWERCURVEAGGREGATIONMSG_WATTSENTRY._options = None
  _POWERCURVEAGGREGATIONMSG_WATTSENTRY._serialized_options = b'8\001'
  _POWERCURVEAGGREGATIONMSG_WATTSPERKGENTRY._options = None
  _POWERCURVEAGGREGATIONMSG_WATTSPERKGENTRY._serialized_options = b'8\001'
  _ACTIVITYPRIVACYTYPE._serialized_start=5805
  _ACTIVITYPRIVACYTYPE._serialized_end=5864
  _SPORT._serialized_start=5866
  _SPORT._serialized_end=5935
  _PLAYERTYPE._serialized_start=5938
  _PLAYERTYPE._serialized_end=6097
  _POWERTYPE._serialized_start=6099
  _POWERTYPE._serialized_end=6165
  _FOLLOWSTATUS._serialized_start=6168
  _FOLLOWSTATUS._serialized_end=6326
  _PLAYERPROFILE._serialized_start=18
  _PLAYERPROFILE._serialized_end=3857
  _PLAYERPROFILE_SOCIALFACTS._serialized_start=3156
  _PLAYERPROFILE_SOCIALFACTS._serialized_end=3451
  _PLAYERPROFILE_REMINDER._serialized_start=3454
  _PLAYERPROFILE_REMINDER._serialized_end=3610
  _PLAYERPROFILE_REMINDER_REMINDERPROPERTY._serialized_start=3556
  _PLAYERPROFILE_REMINDER_REMINDERPROPERTY._serialized_end=3610
  _PLAYERPROFILE_ENROLLEDPROGRAM._serialized_start=3612
  _PLAYERPROFILE_ENROLLEDPROGRAM._serialized_end=3736
  _PLAYERPROFILE_CYCLINGORGANIZATION._serialized_start=3738
  _PLAYERPROFILE_CYCLINGORGANIZATION._serialized_end=3857
  _PLAYERPROFILES._serialized_start=3859
  _PLAYERPROFILES._serialized_end=3909
  _PROFILEENTITLEMENT._serialized_start=3912
  _PROFILEENTITLEMENT._serialized_end=4728
  _PROFILEENTITLEMENT_ENTITLEMENTTYPE._serialized_start=4367
  _PROFILEENTITLEMENT_ENTITLEMENTTYPE._serialized_end=4443
  _PROFILEENTITLEMENT_PROFILEENTITLEMENTSTATUS._serialized_start=4446
  _PROFILEENTITLEMENT_PROFILEENTITLEMENTSTATUS._serialized_end=4591
  _PROFILEENTITLEMENT_PLATFORM._serialized_start=4594
  _PROFILEENTITLEMENT_PLATFORM._serialized_end=4728
  _PROFILEENTITLEMENTS._serialized_start=4730
  _PROFILEENTITLEMENTS._serialized_end=4794
  _SUBSCRIPTION._serialized_start=4797
  _SUBSCRIPTION._serialized_end=5129
  _SUBSCRIPTION_GATEWAY._serialized_start=4903
  _SUBSCRIPTION_GATEWAY._serialized_end=4938
  _SUBSCRIPTION_SUBSCRIPTIONSTATUS._serialized_start=4941
  _SUBSCRIPTION_SUBSCRIPTIONSTATUS._serialized_end=5129
  _PROPERTYCHANGE._serialized_start=5132
  _PROPERTYCHANGE._serialized_end=5282
  _PROPERTYCHANGE_ID._serialized_start=5236
  _PROPERTYCHANGE_ID._serialized_end=5282
  _ATTRIBUTE._serialized_start=5284
  _ATTRIBUTE._serialized_end=5372
  _ACHIEVEMENTENTRY._serialized_start=5374
  _ACHIEVEMENTENTRY._serialized_end=5404
  _ACHIEVEMENTS._serialized_start=5406
  _ACHIEVEMENTS._serialized_end=5461
  _BESTEFFORTPOINTMSG._serialized_start=5463
  _BESTEFFORTPOINTMSG._serialized_end=5517
  _POWERCURVEAGGREGATIONMSG._serialized_start=5520
  _POWERCURVEAGGREGATIONMSG._serialized_end=5803
  _POWERCURVEAGGREGATIONMSG_WATTSENTRY._serialized_start=5666
  _POWERCURVEAGGREGATIONMSG_WATTSENTRY._serialized_end=5731
  _POWERCURVEAGGREGATIONMSG_WATTSPERKGENTRY._serialized_start=5733
  _POWERCURVEAGGREGATIONMSG_WATTSPERKGENTRY._serialized_end=5803
# @@protoc_insertion_point(module_scope)
