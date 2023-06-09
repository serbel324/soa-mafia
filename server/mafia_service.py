import grpc
import mafia_pb2
import mafia_pb2_grpc
from google.protobuf.empty_pb2 import Empty

from room import Room

import typing

class MafiaServerServicer(mafia_pb2_grpc.MafiaServerServicer):
    rooms: typing.Dict[str, Room] = {}

    def CreateRoom(self, request, context):
        name = request.name
        game_size = request.game_size
    
        if len(name) == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            raise ValueError('Name cannot be empty')
        if game_size < 3:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            raise ValueError('game_size must be no less than 3')
        if name in self.rooms.keys():
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            raise ValueError('Room with this name already exists')
            
        self.rooms[name] = Room(name, game_size, request.comment)
        room = self.rooms[name]
        return mafia_pb2.CreateRoomResponse(admin_token=room.admin_token)


    def DeleteRoom(self, request, context):
        room_name = request.room_name
        admin_token = request.admin_token

        room = self.rooms.get(room_name, None)

        if room is None:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            raise ValueError(f'Room with name \"{room_name}\" was not found')
        
        if admin_token != room.admin_token:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            print(f'actual token={room.admin_token}, received token={admin_token}')
            context.set_details('You cannot delete this Room')
            raise ValueError(f'Permission denied')
        
        del self.rooms[room_name]

        return Empty()


    def JoinRoom(self, request, context):
        room_name = request.room_name
        player_name = request.player_name
        player_token = request.player_token

        room = self.rooms.get(room_name, None)

        if room is None:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            print(f'Room {room_name} was not found')
            raise ValueError(f'Room with name \"{room_name}\" was not found')

        try:
            room.add_player(player_name, player_token)
        except ValueError as e:
            print(f'Join error: {e}')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            raise e

        return Empty()


    def GetRoomList(self, request, context):
        return mafia_pb2.GetRoomListResponse(rooms=[room.get_description() for room in self.rooms.values()])

    def GetPlayerList(self, request, context):
        room_name = request.room_name

        room = self.rooms.get(room_name, None)
        if room is None:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            print(f'Room {room_name} was not found')
            raise ValueError(f'Room with name \"{room_name}\" was not found')

        return mafia_pb2.GetPlayerListResponse(players=room.list_players())


    def LeaveRoom(self, request, context):
        room_name = request.room_name
        player_token = request.player_token

        room = self.rooms.get(room_name, None)

        if room is None:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            print(f'Room {room_name} was not found')
            raise ValueError(f'Room with name \"{room_name}\" was not found')

        try:
            room.leave_request(player_token)
        except ValueError as e:
            print(f'Leave error: {e}')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            raise e

        return Empty()
    
    def SubscribeOnNotifications(self, request, context):
        player_token = request.player_token
        room_name = request.room_name
        print(f'Subscribe on notifications, player_token={player_token}, room_name={room_name}')
        while True:
            if self.rooms[room_name].players[player_token].notifications.empty():
                continue
            ntf = self.rooms[room_name].players[player_token].notifications.get()
            yield ntf


    def SignalIsReady(self, request, context):
        player_token = request.player_token
        room_name = request.room_name
        room = self.rooms.get(room_name, None)

        if room is None:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            print(f'Room {room_name} was not found')
            raise ValueError(f'Room with name \"{room_name}\" was not found')

        try:
            room.signal_is_ready(player_token)
        except ValueError as e:
            print(f'Leave error: {e}')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            raise e
        return Empty()
