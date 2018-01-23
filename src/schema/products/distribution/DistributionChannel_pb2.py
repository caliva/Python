# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: products/distribution/DistributionChannel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='products/distribution/DistributionChannel.proto',
  package='opencannabis.products.distribution',
  syntax='proto3',
  serialized_pb=_b('\n/products/distribution/DistributionChannel.proto\x12\"opencannabis.products.distribution\"\xb4\x01\n\x12\x44istributionPolicy\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12<\n\x07\x63hannel\x18\x02 \x01(\x0e\x32+.opencannabis.products.distribution.Channel\x12=\n\x04type\x18\x03 \x01(\x0e\x32/.opencannabis.products.distribution.ChannelType\x12\x10\n\x08suppress\x18\x04 \x01(\x08*G\n\x07\x43hannel\x12\x17\n\x13UNSPECIFIED_CHANNEL\x10\x00\x12\n\n\x06RETAIL\x10\x01\x12\r\n\tWHOLESALE\x10\x02\x12\x08\n\x04\x42ULK\x10\x03*H\n\x0b\x43hannelType\x12\x1c\n\x18UNSPECIFIED_CHANNEL_TYPE\x10\x00\x12\n\n\x06\x44IRECT\x10\x01\x12\x0f\n\x0bMARKETPLACE\x10\x02\x42<\n\x1eio.opencannabis.schema.productB\x13\x44istributionChannelH\x01P\x00\xf8\x01\x01\x62\x06proto3')
)

_CHANNEL = _descriptor.EnumDescriptor(
  name='Channel',
  full_name='opencannabis.products.distribution.Channel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_CHANNEL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETAIL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WHOLESALE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BULK', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=270,
  serialized_end=341,
)
_sym_db.RegisterEnumDescriptor(_CHANNEL)

Channel = enum_type_wrapper.EnumTypeWrapper(_CHANNEL)
_CHANNELTYPE = _descriptor.EnumDescriptor(
  name='ChannelType',
  full_name='opencannabis.products.distribution.ChannelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_CHANNEL_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARKETPLACE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=343,
  serialized_end=415,
)
_sym_db.RegisterEnumDescriptor(_CHANNELTYPE)

ChannelType = enum_type_wrapper.EnumTypeWrapper(_CHANNELTYPE)
UNSPECIFIED_CHANNEL = 0
RETAIL = 1
WHOLESALE = 2
BULK = 3
UNSPECIFIED_CHANNEL_TYPE = 0
DIRECT = 1
MARKETPLACE = 2



_DISTRIBUTIONPOLICY = _descriptor.Descriptor(
  name='DistributionPolicy',
  full_name='opencannabis.products.distribution.DistributionPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='opencannabis.products.distribution.DistributionPolicy.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='opencannabis.products.distribution.DistributionPolicy.channel', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='opencannabis.products.distribution.DistributionPolicy.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suppress', full_name='opencannabis.products.distribution.DistributionPolicy.suppress', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=88,
  serialized_end=268,
)

_DISTRIBUTIONPOLICY.fields_by_name['channel'].enum_type = _CHANNEL
_DISTRIBUTIONPOLICY.fields_by_name['type'].enum_type = _CHANNELTYPE
DESCRIPTOR.message_types_by_name['DistributionPolicy'] = _DISTRIBUTIONPOLICY
DESCRIPTOR.enum_types_by_name['Channel'] = _CHANNEL
DESCRIPTOR.enum_types_by_name['ChannelType'] = _CHANNELTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DistributionPolicy = _reflection.GeneratedProtocolMessageType('DistributionPolicy', (_message.Message,), dict(
  DESCRIPTOR = _DISTRIBUTIONPOLICY,
  __module__ = 'products.distribution.DistributionChannel_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.products.distribution.DistributionPolicy)
  ))
_sym_db.RegisterMessage(DistributionPolicy)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036io.opencannabis.schema.productB\023DistributionChannelH\001P\000\370\001\001'))
# @@protoc_insertion_point(module_scope)
