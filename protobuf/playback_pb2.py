# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: playback.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eplayback.proto\"a\n\x0cPlaybackData\x12\x12\n\nsegment_id\x18\x01 \x02(\x03\x12\x0c\n\x04time\x18\x03 \x02(\x02\x12\x12\n\nworld_time\x18\x04 \x02(\x04\x12\x1b\n\x04type\x18\x0b \x01(\x0e\x32\r.PlaybackType\"\x80\x01\n\x10PlaybackMetadata\x12\x0c\n\x04uuid\x18\x01 \x02(\t\x12\x12\n\nsegment_id\x18\x02 \x02(\x03\x12\x0c\n\x04time\x18\x04 \x02(\x02\x12\x12\n\nworld_time\x18\x05 \x02(\x04\x12\x0b\n\x03url\x18\x06 \x02(\t\x12\x1b\n\x04type\x18\x08 \x01(\x0e\x32\r.PlaybackType*&\n\x0cPlaybackType\x12\x0b\n\x07SEGMENT\x10\x00\x12\t\n\x05ROUTE\x10\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'playback_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYBACKTYPE._serialized_start=248
  _PLAYBACKTYPE._serialized_end=286
  _PLAYBACKDATA._serialized_start=18
  _PLAYBACKDATA._serialized_end=115
  _PLAYBACKMETADATA._serialized_start=118
  _PLAYBACKMETADATA._serialized_end=246
# @@protoc_insertion_point(module_scope)