# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_testauth/ping.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18grpc_testauth/ping.proto\x12\x12grpc_testauth.ping\"j\n\x04Ping\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x19\n\x11\x66\x63_character_name\x18\x04 \x01(\t\x12\x17\n\x0f\x66\x63_character_id\x18\x05 \x01(\r\"\"\n\x11PingSearchRequest\x12\r\n\x05token\x18\x01 \x01(\t\"M\n\x12PingSearchResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12&\n\x04ping\x18\x02 \x01(\x0b\x32\x18.grpc_testauth.ping.Pingb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_testauth.ping_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PING._serialized_start=48
  _PING._serialized_end=154
  _PINGSEARCHREQUEST._serialized_start=156
  _PINGSEARCHREQUEST._serialized_end=190
  _PINGSEARCHRESPONSE._serialized_start=192
  _PINGSEARCHRESPONSE._serialized_end=269
# @@protoc_insertion_point(module_scope)
