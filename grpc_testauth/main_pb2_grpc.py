# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from grpc_testauth import group_pb2 as grpc__testauth_dot_group__pb2
from grpc_testauth import user_pb2 as grpc__testauth_dot_user__pb2


class GroupServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Search = channel.unary_unary(
        '/grpc_testauth.GroupService/Search',
        request_serializer=grpc__testauth_dot_group__pb2.GroupSearchRequest.SerializeToString,
        response_deserializer=grpc__testauth_dot_group__pb2.GroupSearchResponse.FromString,
        )


class GroupServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Search(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GroupServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Search': grpc.unary_unary_rpc_method_handler(
          servicer.Search,
          request_deserializer=grpc__testauth_dot_group__pb2.GroupSearchRequest.FromString,
          response_serializer=grpc__testauth_dot_group__pb2.GroupSearchResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc_testauth.GroupService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class UserServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Search = channel.unary_unary(
        '/grpc_testauth.UserService/Search',
        request_serializer=grpc__testauth_dot_user__pb2.UserSearchRequest.SerializeToString,
        response_deserializer=grpc__testauth_dot_user__pb2.UserSearchRequest.FromString,
        )


class UserServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Search(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Search': grpc.unary_unary_rpc_method_handler(
          servicer.Search,
          request_deserializer=grpc__testauth_dot_user__pb2.UserSearchRequest.FromString,
          response_serializer=grpc__testauth_dot_user__pb2.UserSearchRequest.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc_testauth.UserService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))