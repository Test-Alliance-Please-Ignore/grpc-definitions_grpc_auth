# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: grpc_testauth/main.proto
# plugin: grpclib.plugin.main
import abc

import grpclib.const
import grpclib.client

import grpc_testauth.group_pb2
import grpc_testauth.user_pb2
import grpc_testauth.main_pb2


class GroupServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Search(self, stream):
        pass

    def __mapping__(self):
        return {
            '/grpc_testauth.GroupService/Search': grpclib.const.Handler(
                self.Search,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpc_testauth.group_pb2.GroupSearchRequest,
                grpc_testauth.group_pb2.GroupSearchResponse,
            ),
        }


class GroupServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Search = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpc_testauth.GroupService/Search',
            grpc_testauth.group_pb2.GroupSearchRequest,
            grpc_testauth.group_pb2.GroupSearchResponse,
        )


class UserServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Search(self, stream):
        pass

    @abc.abstractmethod
    async def ServiceSearch(self, stream):
        pass

    def __mapping__(self):
        return {
            '/grpc_testauth.UserService/Search': grpclib.const.Handler(
                self.Search,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpc_testauth.user_pb2.UserSearchRequest,
                grpc_testauth.user_pb2.UserSearchResponse,
            ),
            '/grpc_testauth.UserService/ServiceSearch': grpclib.const.Handler(
                self.ServiceSearch,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpc_testauth.user_pb2.UserServiceSearchRequest,
                grpc_testauth.user_pb2.UserSearchResponse,
            ),
        }


class UserServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Search = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpc_testauth.UserService/Search',
            grpc_testauth.user_pb2.UserSearchRequest,
            grpc_testauth.user_pb2.UserSearchResponse,
        )
        self.ServiceSearch = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpc_testauth.UserService/ServiceSearch',
            grpc_testauth.user_pb2.UserServiceSearchRequest,
            grpc_testauth.user_pb2.UserSearchResponse,
        )