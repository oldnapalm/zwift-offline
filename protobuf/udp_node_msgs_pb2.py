# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: udp-node-msgs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import profile_pb2 as profile__pb2
import per_session_info_pb2 as per__session__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13udp-node-msgs.proto\x1a\rprofile.proto\x1a\x16per-session-info.proto\"\xb6\x02\n\x0eWorldAttribute\x12\r\n\x05wa_f1\x18\x01 \x01(\x03\x12\x14\n\x0cserver_realm\x18\x02 \x01(\x03\x12\x19\n\x07wa_type\x18\x03 \x01(\x0e\x32\x08.WA_TYPE\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x12\x17\n\x0fworld_time_born\x18\x05 \x01(\x03\x12\t\n\x01x\x18\x06 \x01(\x03\x12\x12\n\ny_altitude\x18\x07 \x01(\x03\x12\t\n\x01z\x18\x08 \x01(\x03\x12\x19\n\x11world_time_expire\x18\t \x01(\x03\x12\x0e\n\x06rel_id\x18\n \x01(\x03\x12\x12\n\nimportance\x18\x0b \x01(\x05\x12\x0e\n\x06wa_f12\x18\x0c \x01(\x03\x12\x0e\n\x06wa_f13\x18\r \x01(\x05\x12\x11\n\ttimestamp\x18\x0e \x01(\x03\x12\x0e\n\x06wa_f15\x18\x0f \x01(\x05\x12\x0e\n\x06wa_f16\x18\x10 \x01(\x03\"\x91\x05\n\x0bPlayerState\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tworldTime\x18\x02 \x01(\x03\x12\x10\n\x08\x64istance\x18\x03 \x01(\x05\x12\x10\n\x08roadTime\x18\x04 \x01(\x05\x12\x0c\n\x04laps\x18\x05 \x01(\x05\x12\r\n\x05speed\x18\x06 \x01(\r\x12\r\n\x05ps_f7\x18\x07 \x01(\r\x12\x14\n\x0croadPosition\x18\x08 \x01(\x05\x12\x12\n\ncadenceUHz\x18\t \x01(\x05\x12\x0e\n\x06ps_f10\x18\n \x01(\x05\x12\x11\n\theartrate\x18\x0b \x01(\x05\x12\r\n\x05power\x18\x0c \x01(\x05\x12\x0f\n\x07heading\x18\r \x01(\x03\x12\x0c\n\x04lean\x18\x0e \x01(\x03\x12\x10\n\x08\x63limbing\x18\x0f \x01(\x05\x12\x0c\n\x04time\x18\x10 \x01(\x05\x12\x0e\n\x06ps_f17\x18\x11 \x01(\x05\x12\x10\n\x08\x66rameHue\x18\x12 \x01(\r\x12\x0b\n\x03\x66\x31\x39\x18\x13 \x01(\r\x12\x0b\n\x03\x66\x32\x30\x18\x14 \x01(\r\x12\x10\n\x08progress\x18\x15 \x01(\r\x12\x17\n\x0f\x63ustomizationId\x18\x16 \x01(\x03\x12\x14\n\x0cjustWatching\x18\x17 \x01(\x08\x12\x10\n\x08\x63\x61lories\x18\x18 \x01(\x05\x12\t\n\x01x\x18\x19 \x01(\x02\x12\x12\n\ny_altitude\x18\x1a \x01(\x02\x12\t\n\x01z\x18\x1b \x01(\x02\x12\x17\n\x0fwatchingRiderId\x18\x1c \x01(\x03\x12\x0f\n\x07groupId\x18\x1d \x01(\x03\x12\x15\n\x05sport\x18\x1f \x01(\x0e\x32\x06.Sport\x12\x0e\n\x06ps_f32\x18  \x01(\x02\x12\x0e\n\x06ps_f33\x18! \x01(\r\x12\x0e\n\x06ps_f34\x18\" \x01(\x02\x12\r\n\x05world\x18# \x01(\x05\x12\x0e\n\x06ps_f36\x18$ \x01(\r\x12\x0e\n\x06ps_f37\x18% \x01(\r\x12\x10\n\x08\x63\x61nSteer\x18& \x01(\x08\x12\r\n\x05route\x18\' \x01(\x05\"\xcd\x02\n\x0e\x43lientToServer\x12\x14\n\x0cserver_realm\x18\x01 \x02(\x03\x12\x11\n\tplayer_id\x18\x02 \x02(\x03\x12\x12\n\nworld_time\x18\x03 \x01(\x03\x12\r\n\x05seqno\x18\x04 \x01(\r\x12\x0e\n\x06\x63ts_f5\x18\x05 \x01(\r\x12\x0e\n\x06\x63ts_f6\x18\x06 \x01(\x03\x12\x1b\n\x05state\x18\x07 \x02(\x0b\x32\x0c.PlayerState\x12\x0e\n\x06\x63ts_f8\x18\x08 \x01(\x08\x12\x0e\n\x06\x63ts_f9\x18\t \x01(\x08\x12\x13\n\x0blast_update\x18\n \x02(\x03\x12\x0f\n\x07\x63ts_f11\x18\x0b \x01(\x08\x12\x1a\n\x12last_player_update\x18\x0c \x02(\x03\x12\x14\n\x0clarg_wa_time\x18\r \x01(\x03\x12\x0f\n\x07\x63ts_f14\x18\x0e \x01(\x08\x12\x14\n\x0csubsSegments\x18\x0f \x03(\x03\x12\x13\n\x0bunsSegments\x18\x10 \x03(\x03\"S\n\rPlayerSummary\x12\x0f\n\x07plsu_f1\x18\x01 \x01(\x05\x12\x0f\n\x07plsu_f2\x18\x02 \x01(\x05\x12\x0f\n\x07plsu_f3\x18\x03 \x01(\x05\x12\x0f\n\x07plsu_f4\x18\x04 \x01(\x05\"\xb9\x01\n\x0fPlayerSummaries\x12\x10\n\x08plsus_f1\x18\x01 \x01(\x12\x12\x10\n\x08plsus_f2\x18\x02 \x01(\x12\x12\x10\n\x08plsus_f3\x18\x03 \x01(\x11\x12\x10\n\x08plsus_f4\x18\x04 \x01(\x11\x12\x10\n\x08plsus_f5\x18\x05 \x01(\x05\x12\x10\n\x08plsus_f6\x18\x06 \x01(\x05\x12\x10\n\x08plsus_f7\x18\x07 \x01(\x05\x12(\n\x10player_summaries\x18\x08 \x03(\x0b\x32\x0e.PlayerSummary\"k\n\x0cRelayAddress\x12\x10\n\x08lb_realm\x18\x01 \x01(\x05\x12\x11\n\tlb_course\x18\x02 \x01(\x05\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\r\n\x05ra_f5\x18\x05 \x01(\x02\x12\r\n\x05ra_f6\x18\x06 \x01(\x02\"`\n\tUdpConfig\x12&\n\x0frelay_addresses\x18\x01 \x03(\x0b\x32\r.RelayAddress\x12\r\n\x05uc_f2\x18\x02 \x01(\x05\x12\r\n\x05uc_f3\x18\x03 \x01(\x05\x12\r\n\x05uc_f4\x18\x04 \x01(\x05\"p\n\x11RelayAddressesVOD\x12\x10\n\x08lb_realm\x18\x01 \x01(\x05\x12\x11\n\tlb_course\x18\x02 \x01(\x05\x12&\n\x0frelay_addresses\x18\x03 \x03(\x0b\x32\r.RelayAddress\x12\x0e\n\x06rav_f4\x18\x04 \x01(\x08\"\x8d\x01\n\x0cUdpConfigVOD\x12/\n\x13relay_addresses_vod\x18\x01 \x03(\x0b\x32\x12.RelayAddressesVOD\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0e\n\x06ucv_f3\x18\x03 \x01(\x03\x12\x0e\n\x06ucv_f4\x18\x04 \x01(\x03\x12\x0e\n\x06ucv_f5\x18\x05 \x01(\x02\x12\x0e\n\x06ucv_f6\x18\x06 \x01(\x02\"E\n\x13PlayerRouteDistance\x12\x0e\n\x06\x62ikeId\x18\x01 \x01(\x05\x12\x0e\n\x06prd_f2\x18\x02 \x01(\x02\x12\x0e\n\x06prd_f3\x18\x03 \x01(\x05\"\xa2\x02\n\x17\x45ventSubgroupPlacements\x12\x0e\n\x06\x65sp_f1\x18\x01 \x01(\x05\x12(\n\nplayer_rd1\x18\x02 \x03(\x0b\x32\x14.PlayerRouteDistance\x12(\n\nplayer_rd2\x18\x03 \x03(\x0b\x32\x14.PlayerRouteDistance\x12(\n\nplayer_rd3\x18\x04 \x03(\x0b\x32\x14.PlayerRouteDistance\x12(\n\nplayer_rd4\x18\x05 \x03(\x0b\x32\x14.PlayerRouteDistance\x12\x18\n\x10\x65ventTotalRiders\x18\x06 \x01(\x05\x12\x15\n\rbikeNetworkId\x18\x07 \x01(\x05\x12\x0e\n\x06\x65sp_f8\x18\x08 \x01(\x05\x12\x0e\n\x06\x65sp_f9\x18\t \x01(\x02\"\xc5\x05\n\x0eServerToClient\x12\x14\n\x0cserver_realm\x18\x01 \x01(\x03\x12\x11\n\tplayer_id\x18\x02 \x01(\x03\x12\x12\n\nworld_time\x18\x03 \x01(\x03\x12\r\n\x05seqno\x18\x04 \x01(\x05\x12\x0e\n\x06stc_f5\x18\x05 \x01(\x05\x12\x1c\n\x06states\x18\x08 \x03(\x0b\x32\x0c.PlayerState\x12 \n\x07updates\x18\t \x03(\x0b\x32\x0f.WorldAttribute\x12\x0f\n\x07stc_f10\x18\n \x03(\x03\x12\x0f\n\x07stc_f11\x18\x0b \x01(\x08\x12\x13\n\x0bzc_local_ip\x18\x0c \x01(\t\x12\x0f\n\x07stc_f13\x18\r \x01(\x03\x12\x10\n\x08zwifters\x18\x0e \x01(\x05\x12\x15\n\rzc_local_port\x18\x0f \x01(\x05\x12 \n\x0bzc_protocol\x18\x10 \x01(\x0e\x32\x0b.IPProtocol\x12\x0f\n\x07stc_f17\x18\x11 \x01(\x03\x12\x10\n\x08num_msgs\x18\x12 \x01(\x05\x12\x0e\n\x06msgnum\x18\x13 \x01(\x05\x12\x16\n\x0ehasSimultLogin\x18\x14 \x01(\x08\x12*\n\x10player_summaries\x18\x15 \x01(\x0b\x32\x10.PlayerSummaries\x12\x30\n\x0e\x65v_subgroup_ps\x18\x17 \x01(\x0b\x32\x18.EventSubgroupPlacements\x12\x1e\n\nudp_config\x18\x18 \x01(\x0b\x32\n.UdpConfig\x12\'\n\x10udp_config_vod_1\x18\x19 \x01(\x0b\x32\r.UdpConfigVOD\x12\x0f\n\x07stc_f26\x18\x1a \x01(\x05\x12\'\n\x10udp_config_vod_2\x18\x1b \x01(\x0b\x32\r.UdpConfigVOD\x12#\n\rplayer_states\x18\x1c \x03(\x0b\x32\x0c.PlayerState\x12\x1e\n\ntcp_config\x18\x1d \x01(\x0b\x32\n.TcpConfig\x12\x13\n\x0b\x61\x63kSubsSegm\x18\x1e \x03(\x03\"8\n\x05Ghost\x12\x11\n\tplayer_id\x18\x01 \x02(\x05\x12\x1c\n\x06states\x18\x02 \x03(\x0b\x32\x0c.PlayerState\" \n\x06Ghosts\x12\x16\n\x06ghosts\x18\x01 \x03(\x0b\x32\x06.Ghost\"k\n\x06RideOn\x12\x11\n\tplayer_id\x18\x01 \x02(\x03\x12\x14\n\x0cto_player_id\x18\x02 \x02(\x03\x12\x11\n\tfirstName\x18\x03 \x02(\t\x12\x10\n\x08lastName\x18\x04 \x02(\t\x12\x13\n\x0b\x63ountryCode\x18\x05 \x02(\x05* \n\x11ZofflineConstants\x12\x0b\n\x07RealmID\x10\x01*\x92\x03\n\x07WA_TYPE\x12\r\n\tWAT_LEAVE\x10\x02\x12\x0f\n\x0bWAT_RELOGIN\x10\x03\x12\x0f\n\x0bWAT_RIDE_ON\x10\x04\x12\x0b\n\x07WAT_SPA\x10\x05\x12\r\n\tWAT_EVENT\x10\x06\x12\x0e\n\nWAT_JOIN_E\x10\x07\x12\x0e\n\nWAT_LEFT_E\x10\x08\x12\x0f\n\x0bWAT_RQ_PROF\x10\t\x12\r\n\tWAT_INV_W\x10\n\x12\x0e\n\nWAT_KICKED\x10\x0b\x12\r\n\tWAT_WTIME\x10\x64\x12\r\n\tWAT_RTIME\x10\x65\x12\r\n\tWAT_B_ACT\x10\x66\x12\r\n\tWAT_GRP_M\x10g\x12\r\n\tWAT_PRI_M\x10h\x12\n\n\x06WAT_SR\x10i\x12\x0c\n\x08WAT_FLAG\x10j\x12\x0c\n\x08WAT_NONE\x10k\x12\x0b\n\x07WAT_RLA\x10l\x12\n\n\x06WAT_GE\x10m\x12\n\n\x06WAT_NM\x10n\x12\x0c\n\x08WAT_LATE\x10o\x12\n\n\x06WAT_RH\x10p\x12\r\n\tWAT_STATS\x10q\x12\r\n\tWAT_FENCE\x10r\x12\r\n\tWAT_BN_GE\x10s\x12\x0b\n\x07WAT_PPI\x10t*\x1e\n\nIPProtocol\x12\x07\n\x03UDP\x10\x01\x12\x07\n\x03TCP\x10\x02')

_ZOFFLINECONSTANTS = DESCRIPTOR.enum_types_by_name['ZofflineConstants']
ZofflineConstants = enum_type_wrapper.EnumTypeWrapper(_ZOFFLINECONSTANTS)
_WA_TYPE = DESCRIPTOR.enum_types_by_name['WA_TYPE']
WA_TYPE = enum_type_wrapper.EnumTypeWrapper(_WA_TYPE)
_IPPROTOCOL = DESCRIPTOR.enum_types_by_name['IPProtocol']
IPProtocol = enum_type_wrapper.EnumTypeWrapper(_IPPROTOCOL)
RealmID = 1
WAT_LEAVE = 2
WAT_RELOGIN = 3
WAT_RIDE_ON = 4
WAT_SPA = 5
WAT_EVENT = 6
WAT_JOIN_E = 7
WAT_LEFT_E = 8
WAT_RQ_PROF = 9
WAT_INV_W = 10
WAT_KICKED = 11
WAT_WTIME = 100
WAT_RTIME = 101
WAT_B_ACT = 102
WAT_GRP_M = 103
WAT_PRI_M = 104
WAT_SR = 105
WAT_FLAG = 106
WAT_NONE = 107
WAT_RLA = 108
WAT_GE = 109
WAT_NM = 110
WAT_LATE = 111
WAT_RH = 112
WAT_STATS = 113
WAT_FENCE = 114
WAT_BN_GE = 115
WAT_PPI = 116
UDP = 1
TCP = 2


_WORLDATTRIBUTE = DESCRIPTOR.message_types_by_name['WorldAttribute']
_PLAYERSTATE = DESCRIPTOR.message_types_by_name['PlayerState']
_CLIENTTOSERVER = DESCRIPTOR.message_types_by_name['ClientToServer']
_PLAYERSUMMARY = DESCRIPTOR.message_types_by_name['PlayerSummary']
_PLAYERSUMMARIES = DESCRIPTOR.message_types_by_name['PlayerSummaries']
_RELAYADDRESS = DESCRIPTOR.message_types_by_name['RelayAddress']
_UDPCONFIG = DESCRIPTOR.message_types_by_name['UdpConfig']
_RELAYADDRESSESVOD = DESCRIPTOR.message_types_by_name['RelayAddressesVOD']
_UDPCONFIGVOD = DESCRIPTOR.message_types_by_name['UdpConfigVOD']
_PLAYERROUTEDISTANCE = DESCRIPTOR.message_types_by_name['PlayerRouteDistance']
_EVENTSUBGROUPPLACEMENTS = DESCRIPTOR.message_types_by_name['EventSubgroupPlacements']
_SERVERTOCLIENT = DESCRIPTOR.message_types_by_name['ServerToClient']
_GHOST = DESCRIPTOR.message_types_by_name['Ghost']
_GHOSTS = DESCRIPTOR.message_types_by_name['Ghosts']
_RIDEON = DESCRIPTOR.message_types_by_name['RideOn']
WorldAttribute = _reflection.GeneratedProtocolMessageType('WorldAttribute', (_message.Message,), {
  'DESCRIPTOR' : _WORLDATTRIBUTE,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:WorldAttribute)
  })
_sym_db.RegisterMessage(WorldAttribute)

PlayerState = _reflection.GeneratedProtocolMessageType('PlayerState', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSTATE,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PlayerState)
  })
_sym_db.RegisterMessage(PlayerState)

ClientToServer = _reflection.GeneratedProtocolMessageType('ClientToServer', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTTOSERVER,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ClientToServer)
  })
_sym_db.RegisterMessage(ClientToServer)

PlayerSummary = _reflection.GeneratedProtocolMessageType('PlayerSummary', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSUMMARY,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PlayerSummary)
  })
_sym_db.RegisterMessage(PlayerSummary)

PlayerSummaries = _reflection.GeneratedProtocolMessageType('PlayerSummaries', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSUMMARIES,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PlayerSummaries)
  })
_sym_db.RegisterMessage(PlayerSummaries)

RelayAddress = _reflection.GeneratedProtocolMessageType('RelayAddress', (_message.Message,), {
  'DESCRIPTOR' : _RELAYADDRESS,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:RelayAddress)
  })
_sym_db.RegisterMessage(RelayAddress)

UdpConfig = _reflection.GeneratedProtocolMessageType('UdpConfig', (_message.Message,), {
  'DESCRIPTOR' : _UDPCONFIG,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:UdpConfig)
  })
_sym_db.RegisterMessage(UdpConfig)

RelayAddressesVOD = _reflection.GeneratedProtocolMessageType('RelayAddressesVOD', (_message.Message,), {
  'DESCRIPTOR' : _RELAYADDRESSESVOD,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:RelayAddressesVOD)
  })
_sym_db.RegisterMessage(RelayAddressesVOD)

UdpConfigVOD = _reflection.GeneratedProtocolMessageType('UdpConfigVOD', (_message.Message,), {
  'DESCRIPTOR' : _UDPCONFIGVOD,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:UdpConfigVOD)
  })
_sym_db.RegisterMessage(UdpConfigVOD)

PlayerRouteDistance = _reflection.GeneratedProtocolMessageType('PlayerRouteDistance', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERROUTEDISTANCE,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PlayerRouteDistance)
  })
_sym_db.RegisterMessage(PlayerRouteDistance)

EventSubgroupPlacements = _reflection.GeneratedProtocolMessageType('EventSubgroupPlacements', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSUBGROUPPLACEMENTS,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:EventSubgroupPlacements)
  })
_sym_db.RegisterMessage(EventSubgroupPlacements)

ServerToClient = _reflection.GeneratedProtocolMessageType('ServerToClient', (_message.Message,), {
  'DESCRIPTOR' : _SERVERTOCLIENT,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ServerToClient)
  })
_sym_db.RegisterMessage(ServerToClient)

Ghost = _reflection.GeneratedProtocolMessageType('Ghost', (_message.Message,), {
  'DESCRIPTOR' : _GHOST,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:Ghost)
  })
_sym_db.RegisterMessage(Ghost)

Ghosts = _reflection.GeneratedProtocolMessageType('Ghosts', (_message.Message,), {
  'DESCRIPTOR' : _GHOSTS,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:Ghosts)
  })
_sym_db.RegisterMessage(Ghosts)

RideOn = _reflection.GeneratedProtocolMessageType('RideOn', (_message.Message,), {
  'DESCRIPTOR' : _RIDEON,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:RideOn)
  })
_sym_db.RegisterMessage(RideOn)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ZOFFLINECONSTANTS._serialized_start=3386
  _ZOFFLINECONSTANTS._serialized_end=3418
  _WA_TYPE._serialized_start=3421
  _WA_TYPE._serialized_end=3823
  _IPPROTOCOL._serialized_start=3825
  _IPPROTOCOL._serialized_end=3855
  _WORLDATTRIBUTE._serialized_start=63
  _WORLDATTRIBUTE._serialized_end=373
  _PLAYERSTATE._serialized_start=376
  _PLAYERSTATE._serialized_end=1033
  _CLIENTTOSERVER._serialized_start=1036
  _CLIENTTOSERVER._serialized_end=1369
  _PLAYERSUMMARY._serialized_start=1371
  _PLAYERSUMMARY._serialized_end=1454
  _PLAYERSUMMARIES._serialized_start=1457
  _PLAYERSUMMARIES._serialized_end=1642
  _RELAYADDRESS._serialized_start=1644
  _RELAYADDRESS._serialized_end=1751
  _UDPCONFIG._serialized_start=1753
  _UDPCONFIG._serialized_end=1849
  _RELAYADDRESSESVOD._serialized_start=1851
  _RELAYADDRESSESVOD._serialized_end=1963
  _UDPCONFIGVOD._serialized_start=1966
  _UDPCONFIGVOD._serialized_end=2107
  _PLAYERROUTEDISTANCE._serialized_start=2109
  _PLAYERROUTEDISTANCE._serialized_end=2178
  _EVENTSUBGROUPPLACEMENTS._serialized_start=2181
  _EVENTSUBGROUPPLACEMENTS._serialized_end=2471
  _SERVERTOCLIENT._serialized_start=2474
  _SERVERTOCLIENT._serialized_end=3183
  _GHOST._serialized_start=3185
  _GHOST._serialized_end=3241
  _GHOSTS._serialized_start=3243
  _GHOSTS._serialized_end=3275
  _RIDEON._serialized_start=3277
  _RIDEON._serialized_end=3384
# @@protoc_insertion_point(module_scope)
