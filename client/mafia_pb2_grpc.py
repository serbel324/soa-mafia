# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import mafia_pb2 as mafia__pb2


class MafiaServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRoom = channel.unary_unary(
                '/Mafia.MafiaServer/CreateRoom',
                request_serializer=mafia__pb2.CreateRoomRequest.SerializeToString,
                response_deserializer=mafia__pb2.CreateRoomResponse.FromString,
                )
        self.DeleteRoom = channel.unary_unary(
                '/Mafia.MafiaServer/DeleteRoom',
                request_serializer=mafia__pb2.DeleteRoomRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetRoomList = channel.unary_unary(
                '/Mafia.MafiaServer/GetRoomList',
                request_serializer=mafia__pb2.GetRoomListRequest.SerializeToString,
                response_deserializer=mafia__pb2.GetRoomListResponse.FromString,
                )
        self.GetPlayerList = channel.unary_unary(
                '/Mafia.MafiaServer/GetPlayerList',
                request_serializer=mafia__pb2.GetPlayerListRequest.SerializeToString,
                response_deserializer=mafia__pb2.GetPlayerListResponse.FromString,
                )
        self.JoinRoom = channel.unary_unary(
                '/Mafia.MafiaServer/JoinRoom',
                request_serializer=mafia__pb2.JoinRoomRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.LeaveRoom = channel.unary_unary(
                '/Mafia.MafiaServer/LeaveRoom',
                request_serializer=mafia__pb2.LeaveRoomRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SignalIsReady = channel.unary_unary(
                '/Mafia.MafiaServer/SignalIsReady',
                request_serializer=mafia__pb2.SignalIsReadyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SubscribeOnNotifications = channel.unary_stream(
                '/Mafia.MafiaServer/SubscribeOnNotifications',
                request_serializer=mafia__pb2.SubscribeOnNotificationsRequest.SerializeToString,
                response_deserializer=mafia__pb2.Notification.FromString,
                )


class MafiaServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoomList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlayerList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LeaveRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignalIsReady(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeOnNotifications(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MafiaServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRoom,
                    request_deserializer=mafia__pb2.CreateRoomRequest.FromString,
                    response_serializer=mafia__pb2.CreateRoomResponse.SerializeToString,
            ),
            'DeleteRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRoom,
                    request_deserializer=mafia__pb2.DeleteRoomRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetRoomList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoomList,
                    request_deserializer=mafia__pb2.GetRoomListRequest.FromString,
                    response_serializer=mafia__pb2.GetRoomListResponse.SerializeToString,
            ),
            'GetPlayerList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlayerList,
                    request_deserializer=mafia__pb2.GetPlayerListRequest.FromString,
                    response_serializer=mafia__pb2.GetPlayerListResponse.SerializeToString,
            ),
            'JoinRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinRoom,
                    request_deserializer=mafia__pb2.JoinRoomRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'LeaveRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.LeaveRoom,
                    request_deserializer=mafia__pb2.LeaveRoomRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SignalIsReady': grpc.unary_unary_rpc_method_handler(
                    servicer.SignalIsReady,
                    request_deserializer=mafia__pb2.SignalIsReadyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SubscribeOnNotifications': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeOnNotifications,
                    request_deserializer=mafia__pb2.SubscribeOnNotificationsRequest.FromString,
                    response_serializer=mafia__pb2.Notification.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Mafia.MafiaServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MafiaServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia.MafiaServer/CreateRoom',
            mafia__pb2.CreateRoomRequest.SerializeToString,
            mafia__pb2.CreateRoomResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia.MafiaServer/DeleteRoom',
            mafia__pb2.DeleteRoomRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRoomList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia.MafiaServer/GetRoomList',
            mafia__pb2.GetRoomListRequest.SerializeToString,
            mafia__pb2.GetRoomListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPlayerList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia.MafiaServer/GetPlayerList',
            mafia__pb2.GetPlayerListRequest.SerializeToString,
            mafia__pb2.GetPlayerListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia.MafiaServer/JoinRoom',
            mafia__pb2.JoinRoomRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LeaveRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia.MafiaServer/LeaveRoom',
            mafia__pb2.LeaveRoomRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignalIsReady(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia.MafiaServer/SignalIsReady',
            mafia__pb2.SignalIsReadyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeOnNotifications(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Mafia.MafiaServer/SubscribeOnNotifications',
            mafia__pb2.SubscribeOnNotificationsRequest.SerializeToString,
            mafia__pb2.Notification.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
