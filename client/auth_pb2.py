# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04\x61uth\"2\n\x0fRegisterRequest\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"!\n\x10RegisterResponse\x12\r\n\x05token\x18\x01 \x01(\t\"/\n\x0cLogInRequest\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1e\n\rLogInResponse\x12\r\n\x05token\x18\x01 \x01(\t2}\n\nAuthServer\x12;\n\x08Register\x12\x15.auth.RegisterRequest\x1a\x16.auth.RegisterResponse\"\x00\x12\x32\n\x05LogIn\x12\x12.auth.LogInRequest\x1a\x13.auth.LogInResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTERREQUEST._serialized_start=20
  _REGISTERREQUEST._serialized_end=70
  _REGISTERRESPONSE._serialized_start=72
  _REGISTERRESPONSE._serialized_end=105
  _LOGINREQUEST._serialized_start=107
  _LOGINREQUEST._serialized_end=154
  _LOGINRESPONSE._serialized_start=156
  _LOGINRESPONSE._serialized_end=186
  _AUTHSERVER._serialized_start=188
  _AUTHSERVER._serialized_end=313
# @@protoc_insertion_point(module_scope)
