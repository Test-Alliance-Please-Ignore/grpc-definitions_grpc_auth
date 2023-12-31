# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_testauth/discord.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from grpc_testauth import user_pb2 as grpc__testauth_dot_user__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_testauth/discord.proto',
  package='grpc_testauth.discord',
  syntax='proto3',
  serialized_pb=_b('\n\x1bgrpc_testauth/discord.proto\x12\x15grpc_testauth.discord\x1a\x18grpc_testauth/user.proto\"T\n\x16LinkDiscordUserRequest\x12&\n\x04user\x18\x01 \x01(\x0b\x32\x18.grpc_testauth.user.User\x12\x12\n\ndiscord_id\x18\x02 \x01(\x03\"*\n\x17LinkDiscordUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[grpc__testauth_dot_user__pb2.DESCRIPTOR,])




_LINKDISCORDUSERREQUEST = _descriptor.Descriptor(
  name='LinkDiscordUserRequest',
  full_name='grpc_testauth.discord.LinkDiscordUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='grpc_testauth.discord.LinkDiscordUserRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discord_id', full_name='grpc_testauth.discord.LinkDiscordUserRequest.discord_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=164,
)


_LINKDISCORDUSERRESPONSE = _descriptor.Descriptor(
  name='LinkDiscordUserResponse',
  full_name='grpc_testauth.discord.LinkDiscordUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc_testauth.discord.LinkDiscordUserResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=208,
)

_LINKDISCORDUSERREQUEST.fields_by_name['user'].message_type = grpc__testauth_dot_user__pb2._USER
DESCRIPTOR.message_types_by_name['LinkDiscordUserRequest'] = _LINKDISCORDUSERREQUEST
DESCRIPTOR.message_types_by_name['LinkDiscordUserResponse'] = _LINKDISCORDUSERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LinkDiscordUserRequest = _reflection.GeneratedProtocolMessageType('LinkDiscordUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _LINKDISCORDUSERREQUEST,
  __module__ = 'grpc_testauth.discord_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.discord.LinkDiscordUserRequest)
  ))
_sym_db.RegisterMessage(LinkDiscordUserRequest)

LinkDiscordUserResponse = _reflection.GeneratedProtocolMessageType('LinkDiscordUserResponse', (_message.Message,), dict(
  DESCRIPTOR = _LINKDISCORDUSERRESPONSE,
  __module__ = 'grpc_testauth.discord_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.discord.LinkDiscordUserResponse)
  ))
_sym_db.RegisterMessage(LinkDiscordUserResponse)


# @@protoc_insertion_point(module_scope)
