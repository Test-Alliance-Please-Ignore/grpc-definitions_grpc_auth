# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_testauth/user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from grpc_testauth import group_pb2 as grpc__testauth_dot_group__pb2
from grpc_testauth import eve_pb2 as grpc__testauth_dot_eve__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_testauth/user.proto',
  package='grpc_testauth.user',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18grpc_testauth/user.proto\x12\x12grpc_testauth.user\x1a\x19grpc_testauth/group.proto\x1a\x17grpc_testauth/eve.proto\"\x93\x02\n\x04User\x12\x0f\n\x07\x61uth_id\x18\x01 \x01(\x05\x12\x10\n\x08sso_uuid\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12@\n\x11primary_character\x18\x04 \x01(\x0b\x32%.grpc_testauth.eve.EVEPlayerCharacter\x12\x39\n\ncharacters\x18\x05 \x03(\x0b\x32%.grpc_testauth.eve.EVEPlayerCharacter\x12\x39\n\x06groups\x18\x06 \x03(\x0b\x32).grpc_testauth.group.GroupMembershipEntry\x12\x1e\n\x16primary_character_name\x18\x07 \x01(\t\"D\n\x18UserServiceSearchRequest\x12\x13\n\x0bservice_uid\x18\x01 \x01(\t\x12\x13\n\x0bservice_api\x18\x02 \x01(\t\"\x92\x01\n\x11UserSearchRequest\x12\x11\n\x07\x61uth_id\x18\x01 \x01(\x05H\x00\x12\x12\n\x08username\x18\x02 \x01(\tH\x00\x12\x12\n\x08sso_uuid\x18\x03 \x01(\tH\x00\x12\x18\n\x0e\x63haracter_name\x18\x04 \x01(\tH\x00\x12\x15\n\x0bservice_uid\x18\x05 \x01(\tH\x00\x42\x11\n\x0fuser_identifier\"O\n\x12UserSearchResponse\x12(\n\x06result\x18\x01 \x01(\x0b\x32\x18.grpc_testauth.user.User\x12\x0f\n\x07success\x18\x02 \x01(\x08\"V\n\x15UserPapMinutesRequest\x12&\n\x04user\x18\x01 \x01(\x0b\x32\x18.grpc_testauth.user.User\x12\x15\n\rupto_datetime\x18\x02 \x01(\x03\"*\n\x16UserPapMinutesResponseJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04\x62\x06proto3')
  ,
  dependencies=[grpc__testauth_dot_group__pb2.DESCRIPTOR,grpc__testauth_dot_eve__pb2.DESCRIPTOR,])




_USER = _descriptor.Descriptor(
  name='User',
  full_name='grpc_testauth.user.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_id', full_name='grpc_testauth.user.User.auth_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sso_uuid', full_name='grpc_testauth.user.User.sso_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='grpc_testauth.user.User.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primary_character', full_name='grpc_testauth.user.User.primary_character', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='characters', full_name='grpc_testauth.user.User.characters', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groups', full_name='grpc_testauth.user.User.groups', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primary_character_name', full_name='grpc_testauth.user.User.primary_character_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=101,
  serialized_end=376,
)


_USERSERVICESEARCHREQUEST = _descriptor.Descriptor(
  name='UserServiceSearchRequest',
  full_name='grpc_testauth.user.UserServiceSearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_uid', full_name='grpc_testauth.user.UserServiceSearchRequest.service_uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_api', full_name='grpc_testauth.user.UserServiceSearchRequest.service_api', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=378,
  serialized_end=446,
)


_USERSEARCHREQUEST = _descriptor.Descriptor(
  name='UserSearchRequest',
  full_name='grpc_testauth.user.UserSearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_id', full_name='grpc_testauth.user.UserSearchRequest.auth_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='grpc_testauth.user.UserSearchRequest.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sso_uuid', full_name='grpc_testauth.user.UserSearchRequest.sso_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='character_name', full_name='grpc_testauth.user.UserSearchRequest.character_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_uid', full_name='grpc_testauth.user.UserSearchRequest.service_uid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
      name='user_identifier', full_name='grpc_testauth.user.UserSearchRequest.user_identifier',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=449,
  serialized_end=595,
)


_USERSEARCHRESPONSE = _descriptor.Descriptor(
  name='UserSearchResponse',
  full_name='grpc_testauth.user.UserSearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='grpc_testauth.user.UserSearchResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc_testauth.user.UserSearchResponse.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=597,
  serialized_end=676,
)


_USERPAPMINUTESREQUEST = _descriptor.Descriptor(
  name='UserPapMinutesRequest',
  full_name='grpc_testauth.user.UserPapMinutesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='grpc_testauth.user.UserPapMinutesRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upto_datetime', full_name='grpc_testauth.user.UserPapMinutesRequest.upto_datetime', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=678,
  serialized_end=764,
)


_USERPAPMINUTESRESPONSE = _descriptor.Descriptor(
  name='UserPapMinutesResponse',
  full_name='grpc_testauth.user.UserPapMinutesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=766,
  serialized_end=808,
)

_USER.fields_by_name['primary_character'].message_type = grpc__testauth_dot_eve__pb2._EVEPLAYERCHARACTER
_USER.fields_by_name['characters'].message_type = grpc__testauth_dot_eve__pb2._EVEPLAYERCHARACTER
_USER.fields_by_name['groups'].message_type = grpc__testauth_dot_group__pb2._GROUPMEMBERSHIPENTRY
_USERSEARCHREQUEST.oneofs_by_name['user_identifier'].fields.append(
  _USERSEARCHREQUEST.fields_by_name['auth_id'])
_USERSEARCHREQUEST.fields_by_name['auth_id'].containing_oneof = _USERSEARCHREQUEST.oneofs_by_name['user_identifier']
_USERSEARCHREQUEST.oneofs_by_name['user_identifier'].fields.append(
  _USERSEARCHREQUEST.fields_by_name['username'])
_USERSEARCHREQUEST.fields_by_name['username'].containing_oneof = _USERSEARCHREQUEST.oneofs_by_name['user_identifier']
_USERSEARCHREQUEST.oneofs_by_name['user_identifier'].fields.append(
  _USERSEARCHREQUEST.fields_by_name['sso_uuid'])
_USERSEARCHREQUEST.fields_by_name['sso_uuid'].containing_oneof = _USERSEARCHREQUEST.oneofs_by_name['user_identifier']
_USERSEARCHREQUEST.oneofs_by_name['user_identifier'].fields.append(
  _USERSEARCHREQUEST.fields_by_name['character_name'])
_USERSEARCHREQUEST.fields_by_name['character_name'].containing_oneof = _USERSEARCHREQUEST.oneofs_by_name['user_identifier']
_USERSEARCHREQUEST.oneofs_by_name['user_identifier'].fields.append(
  _USERSEARCHREQUEST.fields_by_name['service_uid'])
_USERSEARCHREQUEST.fields_by_name['service_uid'].containing_oneof = _USERSEARCHREQUEST.oneofs_by_name['user_identifier']
_USERSEARCHRESPONSE.fields_by_name['result'].message_type = _USER
_USERPAPMINUTESREQUEST.fields_by_name['user'].message_type = _USER
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['UserServiceSearchRequest'] = _USERSERVICESEARCHREQUEST
DESCRIPTOR.message_types_by_name['UserSearchRequest'] = _USERSEARCHREQUEST
DESCRIPTOR.message_types_by_name['UserSearchResponse'] = _USERSEARCHRESPONSE
DESCRIPTOR.message_types_by_name['UserPapMinutesRequest'] = _USERPAPMINUTESREQUEST
DESCRIPTOR.message_types_by_name['UserPapMinutesResponse'] = _USERPAPMINUTESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'grpc_testauth.user_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.user.User)
  ))
_sym_db.RegisterMessage(User)

UserServiceSearchRequest = _reflection.GeneratedProtocolMessageType('UserServiceSearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _USERSERVICESEARCHREQUEST,
  __module__ = 'grpc_testauth.user_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.user.UserServiceSearchRequest)
  ))
_sym_db.RegisterMessage(UserServiceSearchRequest)

UserSearchRequest = _reflection.GeneratedProtocolMessageType('UserSearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _USERSEARCHREQUEST,
  __module__ = 'grpc_testauth.user_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.user.UserSearchRequest)
  ))
_sym_db.RegisterMessage(UserSearchRequest)

UserSearchResponse = _reflection.GeneratedProtocolMessageType('UserSearchResponse', (_message.Message,), dict(
  DESCRIPTOR = _USERSEARCHRESPONSE,
  __module__ = 'grpc_testauth.user_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.user.UserSearchResponse)
  ))
_sym_db.RegisterMessage(UserSearchResponse)

UserPapMinutesRequest = _reflection.GeneratedProtocolMessageType('UserPapMinutesRequest', (_message.Message,), dict(
  DESCRIPTOR = _USERPAPMINUTESREQUEST,
  __module__ = 'grpc_testauth.user_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.user.UserPapMinutesRequest)
  ))
_sym_db.RegisterMessage(UserPapMinutesRequest)

UserPapMinutesResponse = _reflection.GeneratedProtocolMessageType('UserPapMinutesResponse', (_message.Message,), dict(
  DESCRIPTOR = _USERPAPMINUTESRESPONSE,
  __module__ = 'grpc_testauth.user_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.user.UserPapMinutesResponse)
  ))
_sym_db.RegisterMessage(UserPapMinutesResponse)


# @@protoc_insertion_point(module_scope)
