# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fitness.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rfitness.proto\"\x83\x01\n\x07\x46itness\x12\x0e\n\x06streak\x18\x01 \x01(\x05\x12\x1f\n\tthis_week\x18\x02 \x01(\x0b\x32\x0c.WeekMetrics\x12\x1f\n\tlast_week\x18\x03 \x01(\x0b\x32\x0c.WeekMetrics\x12\x1a\n\x05goals\x18\x04 \x01(\x0b\x32\x0b.SportGoals\x12\n\n\x02\x66\x35\x18\x05 \x01(\x05\"\x9a\x01\n\x0bWeekMetrics\x12\r\n\x05start\x18\x01 \x01(\t\x12\n\n\x02\x66\x32\x18\x02 \x01(\x02\x12\x10\n\x08\x64istance\x18\x03 \x01(\x05\x12\n\n\x02\x66\x34\x18\x04 \x01(\x05\x12\n\n\x02\x66\x35\x18\x05 \x01(\x05\x12\x0c\n\x04work\x18\x06 \x01(\x05\x12\x10\n\x08\x63\x61lories\x18\x07 \x01(\x05\x12\x0b\n\x03tss\x18\x08 \x01(\x02\x12\x19\n\x04\x64\x61ys\x18\t \x03(\x0b\x32\x0b.DayMetrics\"\x9c\x01\n\nDayMetrics\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\t\x12\x10\n\x08\x64istance\x18\x02 \x01(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05\x12\n\n\x02\x66\x34\x18\x04 \x01(\x05\x12\x0c\n\x04work\x18\x05 \x01(\x05\x12\x10\n\x08\x63\x61lories\x18\x06 \x01(\x05\x12\x0b\n\x03tss\x18\x07 \x01(\x02\x12*\n\x0bpower_zones\x18\x08 \x03(\x0b\x32\x15.PowerZonePercentages\"8\n\x14PowerZonePercentages\x12\x0c\n\x04zone\x18\x01 \x01(\x05\x12\x12\n\npercentage\x18\x02 \x01(\x02\"R\n\nSportGoals\x12\"\n\x0cgoal_setting\x18\x01 \x01(\x0b\x32\x0c.GoalSetting\x12\n\n\x02\x66\x34\x18\x04 \x01(\x05\x12\x14\n\x0clast_updated\x18\x05 \x01(\x03\"1\n\x0bGoalSetting\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12\n\n\x02\x66\x32\x18\x02 \x01(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fitness_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FITNESS._serialized_start=18
  _FITNESS._serialized_end=149
  _WEEKMETRICS._serialized_start=152
  _WEEKMETRICS._serialized_end=306
  _DAYMETRICS._serialized_start=309
  _DAYMETRICS._serialized_end=465
  _POWERZONEPERCENTAGES._serialized_start=467
  _POWERZONEPERCENTAGES._serialized_end=523
  _SPORTGOALS._serialized_start=525
  _SPORTGOALS._serialized_end=607
  _GOALSETTING._serialized_start=609
  _GOALSETTING._serialized_end=658
# @@protoc_insertion_point(module_scope)
