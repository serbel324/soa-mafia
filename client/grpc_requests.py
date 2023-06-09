import grpc
import auth_pb2
import mafia_pb2

from copy import copy

import typing


class LocalInfo():
    player_name: str = ''
    player_token: str = ''
    owned_rooms: typing.Dict[str, str] = {}

local_info = LocalInfo()

def grpc_register(stub, login: str, password: str) -> bool:
    global local_info
    try:
        req = auth_pb2.RegisterRequest(login=login, password=password)
        res = stub.Register(req)

        local_info.player_name = login
        local_info.player_token = res.token
        return True

    except grpc.RpcError as e:
        print(f'RPC error: code={e.code()} message=\"{e.details()}\"')
        return False


def grpc_log_in(stub, login: str, password: str) -> bool:
    global local_info
    try:
        req = auth_pb2.LogInRequest(login=login, password=password)
        res = stub.LogIn(req)

        local_info.player_name = login
        local_info.player_token = res.token
        return True

    except grpc.RpcError as e:
        print(f'RPC error: code={e.code()} message=\"{e.details()}\"')
        return False


def grpc_create_room(stub, name: str, game_size: int, comment: str = "") -> bool:
    global owned_rooms

    try:
        req = mafia_pb2.CreateRoomRequest(name=name, game_size=game_size, comment=comment)
        res = stub.CreateRoom(req)
        local_info.owned_rooms[name] = res.admin_token
        return True
    except grpc.RpcError as e:
        print(f'RPC error: code={e.code()} message=\"{e.details()}\"')
        return False


def grpc_list_rooms(stub) -> typing.List[mafia_pb2.RoomDescription]:
    try:
        req = mafia_pb2.GetRoomListRequest()
        res = stub.GetRoomList(req)
        return res.rooms
    except grpc.RpcError as e:
        print(f'RPC error: code={e.code()} message=\"{e.details()}\"')
        return None


def grpc_delete_room(stub, name: str, admin_token: str) -> bool:
    try:
        req = mafia_pb2.DeleteRoomRequest(room_name=name, admin_token=admin_token)
        stub.DeleteRoom(req)
        return True
    except grpc.RpcError as e:
        print(f'RPC error: code={e.code()} message=\"{e.details()}\"')
        return False


def grpc_join_room(stub, room_name: str, player_name: str, player_token: str) -> bool:
    try:
        req = mafia_pb2.JoinRoomRequest(room_name=room_name, player_name=player_name, player_token=player_token)
        res = stub.JoinRoom(req)
        return True
    except grpc.RpcError as e:
        print(f'RPC error: code={e.code()} message=\"{e.details()}\"')
        return False
    

def grpc_leave_room(stub, room_name: str, player_token: str) -> bool:
    try:
        req = mafia_pb2.LeaveRoomRequest(room_name=room_name, player_token=player_token)
        stub.LeaveRoom(req)
        return True
    except grpc.RpcError as e:
        print(f'RPC error: code={e.code()} message=\"{e.details()}\"')
        return False


def grpc_list_players(stub, room_name: str) -> typing.List[mafia_pb2.PlayerDescription]:
    try:
        req = mafia_pb2.GetPlayerListRequest(room_name=room_name)
        res = stub.GetPlayerList(req)
        return res.players
    except grpc.RpcError as e:
        print(f'RPC error: code={e.code()} message=\"{e.details()}\"')
        return None


def grpc_signal_ready(stub, room_name: str, player_token: str) -> bool:
    try:
        req = mafia_pb2.SignalIsReadyRequest(room_name=room_name, player_token=player_token)
        stub.SignalIsReady(req)
        return True
    except grpc.RpcError as e:
        print(f'RPC error: code={e.code()} message=\"{e.details()}\"')
        return False


