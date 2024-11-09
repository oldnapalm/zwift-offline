# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: activity.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import profile_pb2 as profile__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61\x63tivity.proto\x1a\rprofile.proto\"\xa3\x01\n\rNotableMoment\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\x04\x12\"\n\x04type\x18\x02 \x01(\x0e\x32\x14.NotableMomentTypeZG\x12\x10\n\x08priority\x18\x03 \x01(\r\x12\x14\n\x0cincidentTime\x18\x04 \x01(\x04\x12\x0c\n\x04\x61ux1\x18\x05 \x01(\t\x12\x0c\n\x04\x61ux2\x18\x06 \x01(\t\x12\x15\n\rlargeImageUrl\x18\x07 \x01(\t\"g\n\x11SocialInteraction\x12\x11\n\tplayer_id\x18\x01 \x01(\x04\x12\x14\n\x0ctimeDuration\x18\x02 \x01(\r\x12\x1a\n\x12proximityTimeScore\x18\x03 \x01(\x02\x12\r\n\x05si_f4\x18\x04 \x01(\t\".\n\x0f\x43lubAttribution\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"?\n\x0fPacePartnerData\x12\x0b\n\x03wkg\x18\x01 \x01(\x02\x12\x0c\n\x04time\x18\x02 \x01(\x02\x12\x11\n\tplayer_id\x18\x03 \x01(\x04\"\xd6\x06\n\x08\x41\x63tivity\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x11\n\tplayer_id\x18\x02 \x02(\x04\x12\x11\n\tcourse_id\x18\x03 \x02(\x04\x12\x0c\n\x04name\x18\x04 \x02(\t\x12\n\n\x02\x66\x35\x18\x05 \x01(\t\x12\x17\n\x0fprivateActivity\x18\x06 \x01(\x08\x12\x12\n\nstart_date\x18\x07 \x02(\t\x12\x10\n\x08\x65nd_date\x18\x08 \x01(\t\x12\x18\n\x10\x64istanceInMeters\x18\t \x01(\x02\x12\x16\n\x0e\x61vg_heart_rate\x18\n \x01(\x02\x12\x16\n\x0emax_heart_rate\x18\x0b \x01(\x02\x12\x11\n\tavg_watts\x18\x0c \x01(\x02\x12\x11\n\tmax_watts\x18\r \x01(\x02\x12\x13\n\x0b\x61vg_cadence\x18\x0e \x01(\x02\x12\x13\n\x0bmax_cadence\x18\x0f \x01(\x02\x12\x11\n\tavg_speed\x18\x10 \x01(\x02\x12\x11\n\tmax_speed\x18\x11 \x01(\x02\x12\x10\n\x08\x63\x61lories\x18\x12 \x01(\x02\x12\x17\n\x0ftotal_elevation\x18\x13 \x01(\x02\x12\x18\n\x10strava_upload_id\x18\x14 \x01(\r\x12\x1a\n\x12strava_activity_id\x18\x15 \x01(\r\x12\x0b\n\x03\x66\x32\x32\x18\x16 \x01(\t\x12\x0b\n\x03\x66\x32\x33\x18\x17 \x01(\r\x12\x0b\n\x03\x66it\x18\x18 \x01(\x0c\x12\x14\n\x0c\x66it_filename\x18\x19 \x01(\t\x12\x12\n\nsubgroupId\x18\x1a \x01(\x04\x12\x13\n\x0bworkoutHash\x18\x1b \x01(\x04\x12\x1a\n\x12progressPercentage\x18\x1c \x01(\x02\x12\x15\n\x05sport\x18\x1d \x01(\x0e\x32\x06.Sport\x12\x0c\n\x04\x64\x61te\x18\x1f \x01(\t\x12\x0f\n\x07\x61\x63t_f32\x18  \x01(\x02\x12\x0f\n\x07\x61\x63t_f33\x18! \x01(\t\x12\x0f\n\x07\x61\x63t_f34\x18\" \x01(\t\x12%\n\x07privacy\x18% \x01(\x0e\x32\x14.ActivityPrivacyType\x12(\n\x0f\x66itness_privacy\x18& \x01(\x0e\x32\x0f.FitnessPrivacy\x12\x11\n\tclub_name\x18\' \x01(\t\x12\x16\n\x0emovingTimeInMs\x18( \x01(\x03\x12\x0c\n\x04work\x18, \x01(\x02\x12\x0b\n\x03tss\x18- \x01(\x02\x12\x18\n\x10normalized_power\x18. \x01(\x02\x12\x13\n\x0bpower_zones\x18\x30 \x03(\r\"-\n\x0c\x41\x63tivityList\x12\x1d\n\nactivities\x18\x01 \x03(\x0b\x32\t.Activity\"1\n\rActivityImage\x12\x13\n\x0b\x61\x63tivity_id\x18\x02 \x02(\x04\x12\x0b\n\x03jpg\x18\x03 \x02(\x0c*\xe5\x02\n\x14NotableMomentTypeZCA\x12\x1d\n\x19NMTC_ACHIEVEMENT_UNLOCKED\x10\x01\x12\x16\n\x12NMTC_UNLOCKED_ITEM\x10\x02\x12\x1a\n\x16NMTC_MISSION_COMPLETED\x10\x03\x12\x1b\n\x17NMTC_FINISHED_CHALLENGE\x10\x04\x12\x19\n\x15NMTC_TOOK_ARCH_JERSEY\x10\x05\x12\x0f\n\x0bNMTC_NEW_PR\x10\x06\x12\x19\n\x15NMTC_MET_DAILY_TARGET\x10\x07\x12\x15\n\x11NMTC_GAINED_LEVEL\x10\x08\x12\x17\n\x13NMTC_COMPLETED_GOAL\x10\t\x12\x17\n\x13NMTC_FINISHED_EVENT\x10\n\x12\x19\n\x15NMTC_FINISHED_WORKOUT\x10\x0b\x12\x10\n\x0cNMTC_RIDE_ON\x10\x0c\x12 \n\x1cNMTC_TRAINING_PLAN_COMPLETED\x10\r*\xf2\x04\n\x17NotableMomentTypeZG_idx\x12\x10\n\x0cNMTI_UNKNOWN\x10\x00\x12\x0f\n\x0bNMTI_NEW_PR\x10\x01\x12\x15\n\x11NMTI_GAINED_LEVEL\x10\x02\x12\x1f\n\x1bNMTI_TRAINING_PLAN_COMPLETE\x10\x03\x12\x16\n\x12NMTI_UNLOCKED_ITEM\x10\x04\x12\x1d\n\x19NMTI_ACHIEVEMENT_UNLOCKED\x10\x05\x12\x1a\n\x16NMTI_MISSION_COMPLETED\x10\x06\x12\x17\n\x13NMTI_COMPLETED_GOAL\x10\x07\x12\x19\n\x15NMTI_MET_DAILY_TARGET\x10\x08\x12\x19\n\x15NMTI_TOOK_ARCH_JERSEY\x10\t\x12\x1b\n\x17NMTI_FINISHED_CHALLENGE\x10\n\x12\x17\n\x13NMTI_FINISHED_EVENT\x10\x0b\x12\x19\n\x15NMTI_FINISHED_WORKOUT\x10\x0c\x12\x17\n\x13NMTI_ACTIVITY_BESTS\x10\r\x12\x0f\n\x0bNMTI_RIDEON\x10\x0e\x12\x13\n\x0fNMTI_RIDEON_INT\x10\x0f\x12\x13\n\x0fNMTI_QUIT_EVENT\x10\x10\x12\x15\n\x11NMTI_USED_POWERUP\x10\x11\x12\x1b\n\x17NMTI_PASSED_TIMING_ARCH\x10\x12\x12\x15\n\x11NMTI_CREATED_GOAL\x10\x13\x12\x15\n\x11NMTI_JOINED_EVENT\x10\x14\x12\x18\n\x14NMTI_STARTED_WORKOUT\x10\x15\x12\x18\n\x14NMTI_STARTED_MISSION\x10\x16\x12\x1f\n\x1bNMTI_HOLIDAY_EVENT_COMPLETE\x10\x17*\xc5\x04\n\x13NotableMomentTypeZG\x12\x0e\n\nNMT_NEW_PR\x10\x00\x12\x14\n\x10NMT_GAINED_LEVEL\x10\x05\x12\x1e\n\x1aNMT_TRAINING_PLAN_COMPLETE\x10\x13\x12\x15\n\x11NMT_UNLOCKED_ITEM\x10\x04\x12\x1c\n\x18NMT_ACHIEVEMENT_UNLOCKED\x10\x02\x12\x19\n\x15NMT_MISSION_COMPLETED\x10\x03\x12\x16\n\x12NMT_COMPLETED_GOAL\x10\n\x12\x18\n\x14NMT_MET_DAILY_TARGET\x10\x01\x12\x18\n\x14NMT_TOOK_ARCH_JERSEY\x10\x08\x12\x1a\n\x16NMT_FINISHED_CHALLENGE\x10\x11\x12\x16\n\x12NMT_FINISHED_EVENT\x10\r\x12\x18\n\x14NMT_FINISHED_WORKOUT\x10\x0f\x12\x16\n\x12NMT_ACTIVITY_BESTS\x10\x14\x12\x0e\n\nNMT_RIDEON\x10\x12\x12\x12\n\x0eNMT_RIDEON_INT\x10\x16\x12\x12\n\x0eNMT_QUIT_EVENT\x10\x0c\x12\x14\n\x10NMT_USED_POWERUP\x10\x06\x12\x1a\n\x16NMT_PASSED_TIMING_ARCH\x10\x07\x12\x14\n\x10NMT_CREATED_GOAL\x10\t\x12\x14\n\x10NMT_JOINED_EVENT\x10\x0b\x12\x17\n\x13NMT_STARTED_WORKOUT\x10\x0e\x12\x17\n\x13NMT_STARTED_MISSION\x10\x10\x12\x1e\n\x1aNMT_HOLIDAY_EVENT_COMPLETE\x10\x15*\xae\x01\n\x13ProfileFollowStatus\x12\x0f\n\x0bPFS_UNKNOWN\x10\x01\x12\x1a\n\x16PFS_REQUESTS_TO_FOLLOW\x10\x02\x12\x14\n\x10PFS_IS_FOLLOWING\x10\x03\x12\x12\n\x0ePFS_IS_BLOCKED\x10\x04\x12\x17\n\x13PFS_NO_RELATIONSHIP\x10\x05\x12\x0c\n\x08PFS_SELF\x10\x06\x12\x19\n\x15PFS_HAS_BEEN_DECLINED\x10\x07*J\n\x0e\x46itnessPrivacy\x12\t\n\x05UNSET\x10\x00\x12\x17\n\x13HIDE_SENSITIVE_DATA\x10\x01\x12\x14\n\x10SAME_AS_ACTIVITY\x10\x02')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'activity_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NOTABLEMOMENTTYPEZCA._serialized_start=1373
  _NOTABLEMOMENTTYPEZCA._serialized_end=1730
  _NOTABLEMOMENTTYPEZG_IDX._serialized_start=1733
  _NOTABLEMOMENTTYPEZG_IDX._serialized_end=2359
  _NOTABLEMOMENTTYPEZG._serialized_start=2362
  _NOTABLEMOMENTTYPEZG._serialized_end=2943
  _PROFILEFOLLOWSTATUS._serialized_start=2946
  _PROFILEFOLLOWSTATUS._serialized_end=3120
  _FITNESSPRIVACY._serialized_start=3122
  _FITNESSPRIVACY._serialized_end=3196
  _NOTABLEMOMENT._serialized_start=34
  _NOTABLEMOMENT._serialized_end=197
  _SOCIALINTERACTION._serialized_start=199
  _SOCIALINTERACTION._serialized_end=302
  _CLUBATTRIBUTION._serialized_start=304
  _CLUBATTRIBUTION._serialized_end=350
  _PACEPARTNERDATA._serialized_start=352
  _PACEPARTNERDATA._serialized_end=415
  _ACTIVITY._serialized_start=418
  _ACTIVITY._serialized_end=1272
  _ACTIVITYLIST._serialized_start=1274
  _ACTIVITYLIST._serialized_end=1319
  _ACTIVITYIMAGE._serialized_start=1321
  _ACTIVITYIMAGE._serialized_end=1370
# @@protoc_insertion_point(module_scope)
