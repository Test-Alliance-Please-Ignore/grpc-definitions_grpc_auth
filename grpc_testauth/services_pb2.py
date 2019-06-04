# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_testauth/services.proto

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
  name='grpc_testauth/services.proto',
  package='grpc_testauth.services',
  syntax='proto3',
  serialized_pb=_b('\n\x1cgrpc_testauth/services.proto\x12\x16grpc_testauth.services\x1a\x18grpc_testauth/user.proto\"\x16\n\x07Service\x12\x0b\n\x03\x61pi\x18\x01 \x01(\t\"\x8f\x01\n\x0eServiceAccount\x12\x30\n\x07service\x18\x01 \x01(\x0b\x32\x1f.grpc_testauth.services.Service\x12&\n\x04user\x18\x02 \x01(\x0b\x32\x18.grpc_testauth.user.User\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\x12\x13\n\x0bservice_uid\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[grpc__testauth_dot_user__pb2.DESCRIPTOR,])




_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='grpc_testauth.services.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api', full_name='grpc_testauth.services.Service.api', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=82,
  serialized_end=104,
)


_SERVICEACCOUNT = _descriptor.Descriptor(
  name='ServiceAccount',
  full_name='grpc_testauth.services.ServiceAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='grpc_testauth.services.ServiceAccount.service', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='grpc_testauth.services.ServiceAccount.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active', full_name='grpc_testauth.services.ServiceAccount.active', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_uid', full_name='grpc_testauth.services.ServiceAccount.service_uid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=107,
  serialized_end=250,
)

_SERVICEACCOUNT.fields_by_name['service'].message_type = _SERVICE
_SERVICEACCOUNT.fields_by_name['user'].message_type = grpc__testauth_dot_user__pb2._USER
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
DESCRIPTOR.message_types_by_name['ServiceAccount'] = _SERVICEACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), dict(
  DESCRIPTOR = _SERVICE,
  __module__ = 'grpc_testauth.services_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.services.Service)
  ))
_sym_db.RegisterMessage(Service)

ServiceAccount = _reflection.GeneratedProtocolMessageType('ServiceAccount', (_message.Message,), dict(
  DESCRIPTOR = _SERVICEACCOUNT,
  __module__ = 'grpc_testauth.services_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.services.ServiceAccount)
  ))
_sym_db.RegisterMessage(ServiceAccount)


# @@protoc_insertion_point(module_scope)