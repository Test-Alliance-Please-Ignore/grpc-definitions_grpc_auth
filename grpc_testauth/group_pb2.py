# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_testauth/group.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_testauth/group.proto',
  package='grpc_testauth.group',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19grpc_testauth/group.proto\x12\x13grpc_testauth.group\"2\n\x05Group\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07sso_urn\x18\x03 \x01(\t\"S\n\x14GroupMembershipEntry\x12)\n\x05group\x18\x01 \x01(\x0b\x32\x1a.grpc_testauth.group.Group\x12\x10\n\x08is_admin\x18\x02 \x01(\x08\"Y\n\x12GroupSearchRequest\x12\x0e\n\x04name\x18\x01 \x01(\tH\x00\x12\x0c\n\x02id\x18\x02 \x01(\x05H\x00\x12\x11\n\x07sso_urn\x18\x03 \x01(\tH\x00\x42\x12\n\x10group_identifier\"R\n\x13GroupSearchResponse\x12*\n\x06result\x18\x01 \x01(\x0b\x32\x1a.grpc_testauth.group.Group\x12\x0f\n\x07success\x18\x02 \x01(\x08\x62\x06proto3')
)




_GROUP = _descriptor.Descriptor(
  name='Group',
  full_name='grpc_testauth.group.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc_testauth.group.Group.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='grpc_testauth.group.Group.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sso_urn', full_name='grpc_testauth.group.Group.sso_urn', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=50,
  serialized_end=100,
)


_GROUPMEMBERSHIPENTRY = _descriptor.Descriptor(
  name='GroupMembershipEntry',
  full_name='grpc_testauth.group.GroupMembershipEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group', full_name='grpc_testauth.group.GroupMembershipEntry.group', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_admin', full_name='grpc_testauth.group.GroupMembershipEntry.is_admin', index=1,
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
  serialized_start=102,
  serialized_end=185,
)


_GROUPSEARCHREQUEST = _descriptor.Descriptor(
  name='GroupSearchRequest',
  full_name='grpc_testauth.group.GroupSearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='grpc_testauth.group.GroupSearchRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc_testauth.group.GroupSearchRequest.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sso_urn', full_name='grpc_testauth.group.GroupSearchRequest.sso_urn', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
      name='group_identifier', full_name='grpc_testauth.group.GroupSearchRequest.group_identifier',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=187,
  serialized_end=276,
)


_GROUPSEARCHRESPONSE = _descriptor.Descriptor(
  name='GroupSearchResponse',
  full_name='grpc_testauth.group.GroupSearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='grpc_testauth.group.GroupSearchResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc_testauth.group.GroupSearchResponse.success', index=1,
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
  serialized_start=278,
  serialized_end=360,
)

_GROUPMEMBERSHIPENTRY.fields_by_name['group'].message_type = _GROUP
_GROUPSEARCHREQUEST.oneofs_by_name['group_identifier'].fields.append(
  _GROUPSEARCHREQUEST.fields_by_name['name'])
_GROUPSEARCHREQUEST.fields_by_name['name'].containing_oneof = _GROUPSEARCHREQUEST.oneofs_by_name['group_identifier']
_GROUPSEARCHREQUEST.oneofs_by_name['group_identifier'].fields.append(
  _GROUPSEARCHREQUEST.fields_by_name['id'])
_GROUPSEARCHREQUEST.fields_by_name['id'].containing_oneof = _GROUPSEARCHREQUEST.oneofs_by_name['group_identifier']
_GROUPSEARCHREQUEST.oneofs_by_name['group_identifier'].fields.append(
  _GROUPSEARCHREQUEST.fields_by_name['sso_urn'])
_GROUPSEARCHREQUEST.fields_by_name['sso_urn'].containing_oneof = _GROUPSEARCHREQUEST.oneofs_by_name['group_identifier']
_GROUPSEARCHRESPONSE.fields_by_name['result'].message_type = _GROUP
DESCRIPTOR.message_types_by_name['Group'] = _GROUP
DESCRIPTOR.message_types_by_name['GroupMembershipEntry'] = _GROUPMEMBERSHIPENTRY
DESCRIPTOR.message_types_by_name['GroupSearchRequest'] = _GROUPSEARCHREQUEST
DESCRIPTOR.message_types_by_name['GroupSearchResponse'] = _GROUPSEARCHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Group = _reflection.GeneratedProtocolMessageType('Group', (_message.Message,), dict(
  DESCRIPTOR = _GROUP,
  __module__ = 'grpc_testauth.group_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.group.Group)
  ))
_sym_db.RegisterMessage(Group)

GroupMembershipEntry = _reflection.GeneratedProtocolMessageType('GroupMembershipEntry', (_message.Message,), dict(
  DESCRIPTOR = _GROUPMEMBERSHIPENTRY,
  __module__ = 'grpc_testauth.group_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.group.GroupMembershipEntry)
  ))
_sym_db.RegisterMessage(GroupMembershipEntry)

GroupSearchRequest = _reflection.GeneratedProtocolMessageType('GroupSearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _GROUPSEARCHREQUEST,
  __module__ = 'grpc_testauth.group_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.group.GroupSearchRequest)
  ))
_sym_db.RegisterMessage(GroupSearchRequest)

GroupSearchResponse = _reflection.GeneratedProtocolMessageType('GroupSearchResponse', (_message.Message,), dict(
  DESCRIPTOR = _GROUPSEARCHRESPONSE,
  __module__ = 'grpc_testauth.group_pb2'
  # @@protoc_insertion_point(class_scope:grpc_testauth.group.GroupSearchResponse)
  ))
_sym_db.RegisterMessage(GroupSearchResponse)


# @@protoc_insertion_point(module_scope)
