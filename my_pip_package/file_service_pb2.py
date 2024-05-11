# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='file_service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x66ile_service.proto\"\'\n\x0b\x41\x64\x64ressPeer\x12\n\n\x02IP\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\"B\n\x0eGetFileRequest\x12\x1d\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x0c.AddressPeer\x12\x11\n\tfile_path\x18\x02 \x01(\t\"8\n\x0fGetFileResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x14\n\x0c\x66ile_content\x18\x02 \x01(\x0c\"X\n\x0eSetFileRequest\x12\x1d\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x0c.AddressPeer\x12\x11\n\tfile_path\x18\x02 \x01(\t\x12\x14\n\x0c\x66ile_content\x18\x03 \x01(\x0c\"\"\n\x0fSetFileResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"A\n\rDeleteRequest\x12\x1d\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x0c.AddressPeer\x12\x11\n\tfile_path\x18\x02 \x01(\t\"!\n\x0e\x44\x65leteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x9e\x01\n\x0b\x46ileService\x12.\n\x07GetFile\x12\x0f.GetFileRequest\x1a\x10.GetFileResponse\"\x00\x12.\n\x07SetFile\x12\x0f.SetFileRequest\x1a\x10.SetFileResponse\"\x00\x12/\n\nDeleteFile\x12\x0e.DeleteRequest\x1a\x0f.DeleteResponse\"\x00\x62\x06proto3'
)




_ADDRESSPEER = _descriptor.Descriptor(
  name='AddressPeer',
  full_name='AddressPeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='IP', full_name='AddressPeer.IP', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='AddressPeer.port', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=22,
  serialized_end=61,
)


_GETFILEREQUEST = _descriptor.Descriptor(
  name='GetFileRequest',
  full_name='GetFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='GetFileRequest.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='GetFileRequest.file_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=63,
  serialized_end=129,
)


_GETFILERESPONSE = _descriptor.Descriptor(
  name='GetFileResponse',
  full_name='GetFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='GetFileResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_content', full_name='GetFileResponse.file_content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=131,
  serialized_end=187,
)


_SETFILEREQUEST = _descriptor.Descriptor(
  name='SetFileRequest',
  full_name='SetFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='SetFileRequest.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='SetFileRequest.file_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_content', full_name='SetFileRequest.file_content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=189,
  serialized_end=277,
)


_SETFILERESPONSE = _descriptor.Descriptor(
  name='SetFileResponse',
  full_name='SetFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='SetFileResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=279,
  serialized_end=313,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='DeleteRequest.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='DeleteRequest.file_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=315,
  serialized_end=380,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='DeleteResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=382,
  serialized_end=415,
)

_GETFILEREQUEST.fields_by_name['address'].message_type = _ADDRESSPEER
_SETFILEREQUEST.fields_by_name['address'].message_type = _ADDRESSPEER
_DELETEREQUEST.fields_by_name['address'].message_type = _ADDRESSPEER
DESCRIPTOR.message_types_by_name['AddressPeer'] = _ADDRESSPEER
DESCRIPTOR.message_types_by_name['GetFileRequest'] = _GETFILEREQUEST
DESCRIPTOR.message_types_by_name['GetFileResponse'] = _GETFILERESPONSE
DESCRIPTOR.message_types_by_name['SetFileRequest'] = _SETFILEREQUEST
DESCRIPTOR.message_types_by_name['SetFileResponse'] = _SETFILERESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddressPeer = _reflection.GeneratedProtocolMessageType('AddressPeer', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSPEER,
  '__module__' : 'file_service_pb2'
  # @@protoc_insertion_point(class_scope:AddressPeer)
  })
_sym_db.RegisterMessage(AddressPeer)

GetFileRequest = _reflection.GeneratedProtocolMessageType('GetFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFILEREQUEST,
  '__module__' : 'file_service_pb2'
  # @@protoc_insertion_point(class_scope:GetFileRequest)
  })
_sym_db.RegisterMessage(GetFileRequest)

GetFileResponse = _reflection.GeneratedProtocolMessageType('GetFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFILERESPONSE,
  '__module__' : 'file_service_pb2'
  # @@protoc_insertion_point(class_scope:GetFileResponse)
  })
_sym_db.RegisterMessage(GetFileResponse)

SetFileRequest = _reflection.GeneratedProtocolMessageType('SetFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETFILEREQUEST,
  '__module__' : 'file_service_pb2'
  # @@protoc_insertion_point(class_scope:SetFileRequest)
  })
_sym_db.RegisterMessage(SetFileRequest)

SetFileResponse = _reflection.GeneratedProtocolMessageType('SetFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETFILERESPONSE,
  '__module__' : 'file_service_pb2'
  # @@protoc_insertion_point(class_scope:SetFileResponse)
  })
_sym_db.RegisterMessage(SetFileResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'file_service_pb2'
  # @@protoc_insertion_point(class_scope:DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'file_service_pb2'
  # @@protoc_insertion_point(class_scope:DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)



_FILESERVICE = _descriptor.ServiceDescriptor(
  name='FileService',
  full_name='FileService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=418,
  serialized_end=576,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFile',
    full_name='FileService.GetFile',
    index=0,
    containing_service=None,
    input_type=_GETFILEREQUEST,
    output_type=_GETFILERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetFile',
    full_name='FileService.SetFile',
    index=1,
    containing_service=None,
    input_type=_SETFILEREQUEST,
    output_type=_SETFILERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteFile',
    full_name='FileService.DeleteFile',
    index=2,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILESERVICE)

DESCRIPTOR.services_by_name['FileService'] = _FILESERVICE

# @@protoc_insertion_point(module_scope)
