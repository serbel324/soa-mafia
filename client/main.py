import logging
import typing
import os
import threading

import grpc
import auth_pb2_grpc
import mafia_pb2_grpc

import asyncio

from grpc_requests import *

from enum import Enum
class StateId(Enum):
    Auth = 1
    Lobby = 2
    Room = 3
    Game = 4

auth_stub: auth_pb2_grpc.AuthServerStub = None
mafia_stub: mafia_pb2_grpc.MafiaServerStub = None

def log_out() -> None:
    global player_token
    player_token = None


def input_cmd() -> typing.Tuple[str, typing.List[str]]:
    a = input().split()
    while len(a) == 0:
        a = input().split()
    cmd = a[0]
    args: typing.List[str] = a[1:]
    return (cmd, args)


def read_more_args(args_num: int) -> typing.List[str]:
    if args_num <= 0:
        return []

    res: typing.List[str] = []
    while len(res) < args_num:
        a = input().split()
        res += a
    return res


class State():
    help_str: str = "Empty"
    cmd: str = None
    id: StateId = None

    def handle_cmd(self, cmd: str, args: typing.List[str]):
        return None
    
    def help(self):
        print(self.help_str)

    def wrong_cmd(self):
        print("Wrong command!")


def subscribe_on_notifications(channel, room_name: str, player_token: str):
    global state
    stub = mafia_pb2_grpc.MafiaServerStub(channel)
    try:
        for event in stub.SubscribeOnNotifications(mafia_pb2.SubscribeOnNotificationsRequest(
            room_name=room_name,
            player_token=player_token
        )):
            if event.is_game_in_progress:
                print_game_state(event.game_state)
            else:
                print_players_list(event.players)
    except Exception as e:
        print(f"Notifications for room {room_name} are disabled")
    channel.close()


def print_players_list(players: typing.List[mafia_pb2.PlayerDescription]) -> None:
    print('Players:')
    for player in players:
        name = player.name
        print(f' * {name}{"(you)" if name == local_info.player_name else ""} {"+" if player.is_ready else "-"}')


def print_game_state(game_state: mafia_pb2.GameState) -> None:
    print('TBD')


class StateAuth(State):
    help_str: str = '''\
+=== Authorization ===+
Create new profile or use an existing one
    * register (login, password) - create new profile
    * login (login, password) - use existing profile
    * quit - quit the application
    * help - show this message
+=== ------------- ===+ \
'''
    id: StateId = StateId.Auth

    def register(self, args: typing.List[str]) -> State:
        args += read_more_args(2 - len(args))
        if grpc_register(auth_stub, args[0], args[1]):
            print(f'Successfully registered as {args[0]}')
            return StateLobby()
        else:
            print(f'Registration fail!')
            return self

    def login(self, args: typing.List[str]) -> State:
        args += read_more_args(2 - len(args))
        if grpc_log_in(auth_stub, args[0], args[1]):
            print(f'Successfully logged in as {args[0]}')
            return StateLobby()
        else:
            print(f'Log in fail!')
            return self

    async def handle_cmd(self, cmd: str, args: typing.List[str]) -> State:
        if cmd == 'login' or cmd == 'l':
            return self.login(args)
        elif cmd == 'register' or cmd == 'r':
            return self.register(args)
        elif cmd == 'help' or cmd == 'h':
            return self
        elif cmd == 'quit' or cmd == 'q':
            return None
        else:
            self.wrong_cmd()
            return self


class StateLobby(State):
    def help(self):
        print(f'''\
+=== [{local_info.player_name}] Main Lobby ===+
Create new room or join existing one
    * create (name, game_size, comment[optional]) - create new room
    * join (name) - use existing profile
    * delete (name) - delete existing room
    * list - get list of existing rooms
    * logout - return to authentification stage
    * quit - quit the application
    * help - show this message
+=== -------------- ===+ \
''')
    id: StateId = StateId.Lobby

    def create(self, args: typing.List[str]) -> State:
        args += read_more_args(2 - len(args))
        args.append('')
        if grpc_create_room(mafia_stub, args[0], int(args[1]), args[2]):
            print(f'Successfully created room \"{args[0]}\"')
            return self
        else:
            print(f'Cannot create room!')
            return self

    def list(self) -> State:
        global local_info
        rooms = grpc_list_rooms(mafia_stub)
        if rooms is not None:
            print('Rooms list:')
            for room in rooms:
                name = room.name
                admin_sign = '*' if name in local_info.owned_rooms.keys() else ''
                print(f' - [{name}] {room.num_players}/{room.game_size} {room.comment} {admin_sign}')
            return self
        else:
            print(f'O_o - Unexpected failure')
            return self

    def delete(self, args: typing.List[str]) -> State:
        global local_info
        args += read_more_args(1 - len(args))
        name = args[0]

        admin_token = local_info.owned_rooms.get(name, None)
        if admin_token is None:
            print(f'You don\'t own room {name}!')
            return self
        
        if grpc_delete_room(mafia_stub, name, admin_token):
            del local_info.owned_rooms[name]
            print('Room deleted successfully')
            return self
        else:
            print(f'Unable to delete room {name}')
            return self
        
    def join(self, args: typing.List[str]):
        args += read_more_args(1 - len(args))
        room_name = args[0]
        if grpc_join_room(mafia_stub, room_name, local_info.player_name, local_info.player_token):
            return StateRoom(room_name)

        else:
            print(f'Unable to join room {room_name}')
            return self


    async def handle_cmd(self, cmd: str, args: typing.List[str]) -> State:
        if cmd == 'create' or cmd == 'c':
            return self.create(args)
        elif cmd == 'join' or cmd == 'j':
            return self.join(args)
        elif cmd == 'delete' or cmd == 'd':
            return self.delete(args)
        elif cmd == 'list' or cmd == 'ls':
            return self.list()
        elif cmd == 'logout' or cmd == 'lo':
            log_out()
            return StateAuth()
        elif cmd == 'help' or cmd == 'h':
            return self
        elif cmd == 'quit' or cmd == 'q':
            return None
        else:
            self.wrong_cmd()
            return self


class StateRoom(State):
    room_name: str = ''
    notification_channel = None

    def __init__(self, room_name: str):
        self.room_name = room_name
        host = os.environ.get('HOST', '0.0.0.0')
        port = os.environ.get('MAFIA_PORT', 5052)
        self.notification_channel = grpc.insecure_channel(f'{host}:{port}')
        notifcations = threading.Thread(target=subscribe_on_notifications, args=(self.notification_channel, self.room_name, local_info.player_token))
        notifcations.start()


    def help(self):
        print(f'''\
+=== [{local_info.player_name}] Room {self.room_name} ===+
Signal when you are ready and wait for other players
    * ready - wait for the beginning of the game
    * leave - leave current room
    * players - list players in current room
    * logout - return to authentification stage
    * quit - quit the application
    * help - show this message
+=== -------------- ===+ \
''')
    id: StateId = StateId.Room
        
    def players(self):
        players = grpc_list_players(mafia_stub, self.room_name)
        if players is not None:
            print_players_list(players)
        else:
            print(f'Cannot list players')
        return self

        
    def leave(self):
        if grpc_leave_room(mafia_stub, self.room_name, local_info.player_token):
            print('Room left')
            self.notification_channel.close()
            return StateLobby()
        else:
            print(f'Unable to leave room - you are doing something wrong')
            return self
        
    def ready(self):
        if grpc_signal_ready(mafia_stub, self.room_name, local_info.player_token):
            print('You are ready to start, waiting for other players')
            return self
        else:
            print(f'Unable to signal readiness - you are doing something wrong')
            return self


    async def handle_cmd(self, cmd: str, args: typing.List[str]) -> State:
        if cmd == 'ready' or cmd == 'r':
            return self.ready()
        elif cmd == 'leave' or cmd == 'l':
            return self.leave()
        elif cmd == 'players' or cmd == 'p':
            return self.players()
        elif cmd == 'logout' or cmd == 'lo':
            log_out()
            return StateAuth()
        elif cmd == 'help' or cmd == 'h':
            return self
        elif cmd == 'quit' or cmd == 'q':
            return None
        else:
            self.wrong_cmd()
            return self

state: State = StateAuth()

async def main_loop():
    global state
    cmd: str = ''
    args: typing.List[str] = []
    while True:
        state.help()
        cmd, args = input_cmd()
        while cmd is None:
            cmd, args = input_cmd()
        state = await state.handle_cmd(cmd, args)
        if state == None:
            return

async def run():
    host = os.environ.get('HOST', '0.0.0.0')
    auth_port = os.environ.get('AUTH_PORT', 5051)
    mafia_port = os.environ.get('MAFIA_PORT', 5052)
    auth_channel = grpc.insecure_channel(f'{host}:{auth_port}')
    mafia_channel = grpc.insecure_channel(f'{host}:{mafia_port}')

    global auth_stub
    global mafia_stub

    auth_stub = auth_pb2_grpc.AuthServerStub(auth_channel)
    mafia_stub = mafia_pb2_grpc.MafiaServerStub(mafia_channel)
    await main_loop()



if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())
