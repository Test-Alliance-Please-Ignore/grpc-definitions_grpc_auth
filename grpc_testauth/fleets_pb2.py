# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_testauth/fleets.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_testauth/fleets.proto',
  package='grpc_testauth.fleets',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1agrpc_testauth/fleets.proto\x12\x14grpc_testauth.fleets\"\x9c\x01\n\x05\x46leet\x12\x11\n\tsrp_token\x18\x01 \x01(\t\x12\x10\n\x08\x66leet_id\x18\x02 \x01(\t\x12\x14\n\x0c\x63\x63p_fleet_id\x18\x03 \x01(\x03\x12\x12\n\ntime_start\x18\x04 \x01(\x03\x12\x10\n\x08time_end\x18\x05 \x01(\x03\x12\x32\n\x07members\x18\x06 \x03(\x0b\x32!.grpc_testauth.fleets.FleetMember\"M\n\x0b\x46leetMember\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x18\n\x10minutes_in_fleet\x18\x02 \x01(\x05\x12\x13\n\x0bjumps_taken\x18\x03 \x01(\x05\"e\n\x14UserFleetListRequest\x12\x12\n\x08username\x18\x01 \x01(\tH\x00\x12\x11\n\x07user_id\x18\x02 \x01(\x05H\x00\x12\x13\n\x0b\x63utoff_date\x18\x03 \x01(\x03\x42\x11\n\x0fuser_identifier\"U\n\x15UserFleetListResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12+\n\x06\x66leets\x18\x02 \x03(\x0b\x32\x1b.grpc_testauth.fleets.Fleetb\x06proto3')
)




_FLEET = _descriptor.Descriptor(
  name='Fleet',
  full_name='grpc_testauth.fleets.Fleet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='srp_token', full_name='grpc_testauth.fleets.Fleet.srp_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fleet_id', full_name='grpc_testauth.fleets.Fleet.fleet_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ccp_fleet_id', full_name='grpc_testauth.fleets.Fleet.ccp_fleet_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_start', full_name='grpc_testauth.fleets.Fleet.time_start', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_end', full_name='grpc_testauth.fleets.Fleet.time_end', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='members', full_name='grpc_testauth.fleets.Fleet.members', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=209,
)


_FLEETMEMBER = _descriptor.Descriptor(
  name='FleetMember',
  full_name='grpc_testauth.fleets.FleetMember',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='grpc_testauth.fleets.FleetMember.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minutes_in_fleet', full_name='grpc_testauth.fleets.FleetMember.minutes_in_fleet', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jumps_taken', full_name='grpc_testauth.fleets.FleetMember.jumps_taken', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=288,
)


_USERFLEETLISTREQUEST = _descriptor.Descriptor(
  name='UserFleetListRequest',
  full_name='grpc_testauth.fleets.UserFleetListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='grpc_testauth.fleets.UserFleetListRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='grpc_testauth.fleets.UserFleetListRequest.user_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cutoff_date', full_name='grpc_testauth.fleets.UserFleetListRequest.cutoff_date', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='user_identifier', full_name='grpc_testauth.fleets.UserFleetListRequest.user_identifier',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=290,
  serialized_end=391,
)


_USERFLEETLISTRESPONSE = _descriptor.Descriptor(
  name='UserFleetListResponse',
  full_name='grpc_testauth.fleets.UserFleetListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc_testauth.fleets.UserFleetListResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fleets', full_name='grpc_testauth.fleets.UserFleetListResponse.fleets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=393,
  serialized_end=478,
)

_FLEET.fields_by_name['members'].message_type = _FLEETMEMBER
_USERFLEETLISTREQUEST.oneofs_by_name['user_identifier'].fields.append(
  _USERFLEETLISTREQUEST.fields_by_name['username'])
_USERFLEETLISTREQUEST.fields_by_name['username'].containing_oneof = _USERFLEETLISTREQUEST.oneofs_by_name['user_identifier']
_USERFLEETLISTREQUEST.oneofs_by_name['user_identifier'].fields.append(
  _USERFLEETLISTREQUEST.fields_by_name['user_id'])
_USERFLEETLISTREQUEST.fields_by_name['user_id'].containing_oneof = _USERFLEETLISTREQUEST.oneofs_by_name['user_identifier']
_USERFLEETLISTRESPONSE.fields_by_name['fleets'].message_type = _FLEET
DESCRIPTOR.message_types_by_name['Fleet'] = _FLEET
DESCRIPTOR.message_types_by_name['FleetMember'] = _FLEETMEMBER
DESCRIPTOR.message_types_by_name['UserFleetListRequest'] = _USERFLEETLISTREQUEST
DESCRIPTOR.message_types_by_name['UserFleetListResponse'] = _USERFLEETLISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Fleet = _reflection.GeneratedProtocolMessageType('Fleet', (_message.Message,), dict(
  DESCRIPTOR = _FLEET,
  __module__ = 'grpc_testauth.fleets_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.fleets.Fleet)
  ))
_sym_db.RegisterMessage(Fleet)

FleetMember = _reflection.GeneratedProtocolMessageType('FleetMember', (_message.Message,), dict(
  DESCRIPTOR = _FLEETMEMBER,
  __module__ = 'grpc_testauth.fleets_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.fleets.FleetMember)
  ))
_sym_db.RegisterMessage(FleetMember)

UserFleetListRequest = _reflection.GeneratedProtocolMessageType('UserFleetListRequest', (_message.Message,), dict(
  DESCRIPTOR = _USERFLEETLISTREQUEST,
  __module__ = 'grpc_testauth.fleets_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.fleets.UserFleetListRequest)
  ))
_sym_db.RegisterMessage(UserFleetListRequest)

UserFleetListResponse = _reflection.GeneratedProtocolMessageType('UserFleetListResponse', (_message.Message,), dict(
  DESCRIPTOR = _USERFLEETLISTRESPONSE,
  __module__ = 'grpc_testauth.fleets_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.fleets.UserFleetListResponse)
  ))
_sym_db.RegisterMessage(UserFleetListResponse)


# @@protoc_insertion_point(module_scope)
