# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_testauth/main.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from grpc_testauth import group_pb2 as grpc__testauth_dot_group__pb2
from grpc_testauth import user_pb2 as grpc__testauth_dot_user__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_testauth/main.proto',
  package='grpc_testauth',
  syntax='proto3',
  serialized_pb=_b('\n\x18grpc_testauth/main.proto\x12\rgrpc_testauth\x1a\x19grpc_testauth/group.proto\x1a\x18grpc_testauth/user.proto2k\n\x0cGroupService\x12[\n\x06Search\x12\'.grpc_testauth.group.GroupSearchRequest\x1a(.grpc_testauth.group.GroupSearchResponse2e\n\x0bUserService\x12V\n\x06Search\x12%.grpc_testauth.user.UserSearchRequest\x1a%.grpc_testauth.user.UserSearchRequestb\x06proto3')
  ,
  dependencies=[grpc__testauth_dot_group__pb2.DESCRIPTOR,grpc__testauth_dot_user__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GROUPSERVICE = _descriptor.ServiceDescriptor(
  name='GroupService',
  full_name='grpc_testauth.GroupService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=96,
  serialized_end=203,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='grpc_testauth.GroupService.Search',
    index=0,
    containing_service=None,
    input_type=grpc__testauth_dot_group__pb2._GROUPSEARCHREQUEST,
    output_type=grpc__testauth_dot_group__pb2._GROUPSEARCHRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GROUPSERVICE)

DESCRIPTOR.services_by_name['GroupService'] = _GROUPSERVICE


_USERSERVICE = _descriptor.ServiceDescriptor(
  name='UserService',
  full_name='grpc_testauth.UserService',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=205,
  serialized_end=306,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='grpc_testauth.UserService.Search',
    index=0,
    containing_service=None,
    input_type=grpc__testauth_dot_user__pb2._USERSEARCHREQUEST,
    output_type=grpc__testauth_dot_user__pb2._USERSEARCHREQUEST,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERSERVICE)

DESCRIPTOR.services_by_name['UserService'] = _USERSERVICE

# @@protoc_insertion_point(module_scope)