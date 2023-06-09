import typing
import queue

ADMIN_TOKEN_LENGTH = 32
ADMIN_TOKEN_CHARS = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'


import mafia_pb2
from token_generator import generate_token


class Player():
    ####### In Room #######
    name: str = ''
    token: str = ''
    is_ready: bool = False

    ####### In Game #######
    role: mafia_pb2.Role = mafia_pb2.Civilian
    is_alive: bool = True
    votes_for: int = 0

    notifications: queue.Queue = None

    def __init__(self, name: str, token: str):
        self.name = name
        self.token = token
        self.notifications = queue.Queue()


class Game():
    game_size: int = 0
    players: typing.List[Player] = []
    def __init__(self, game_size: int, players: typing.List[Player]):
        self.game_size = game_size
        self.players = players

        mafia_count = 1 if game_size < 7 else 2
        sheriff_count = 1


    def get_state(self, player_token: str) -> mafia_pb2.GameState:
        ret = mafia_pb2.GameState()
        player = self.players[player_token]
        if player.role == mafia_pb2.Role.Civilian:
            ret.players = [mafia_pb2.Player(name=x.name, votes_for=x.votes_for, is_alive=x.is_alive) for x in self.players]

        return ret


class Room():
    name: str = None
    game_size: int = None
    comment: str = None
    admin_token: str = None
    players: typing.Dict[str, Player] = {}
    players_ready: int
    game: Game = None

    def __init__(self, name: str, game_size: int, comment: str):
        self.name = name
        self.game_size = game_size
        self.comment = comment if comment is not None else ''
        self.players = {}
        self.game = None
        self.players_ready = 0 
        self.admin_token = generate_token(ADMIN_TOKEN_LENGTH, ADMIN_TOKEN_CHARS)


    def add_player(self, name: str, token: str) -> None:
        if len(self.players) == self.game_size:
            raise ValueError('Room is already full!')
        if token in self.players.keys():
            raise ValueError(f'This player has already joined')


        self.players[token] = Player(name, token)

        for player in self.players.values():
            player.notifications.put(mafia_pb2.Notification(players=self.list_players(), is_game_in_progress=False))


    def leave_request(self, token: str) -> None:
        if token not in self.players.keys():
            raise ValueError(f'Player with given token was not found')
        del self.players[token]


    def signal_is_ready(self, token: str) -> None:
        if token not in self.players.keys():
            raise ValueError(f'Player with given token was not found')
        self.players[token].is_ready = True
        self.players_ready += 1
        if self.players_ready == self.game_size:
            self.start_game()

    def get_description(self) -> mafia_pb2.RoomDescription:
        return mafia_pb2.RoomDescription(name=self.name, comment=self.comment, num_players=len(self.players), game_size=self.game_size)

    def list_players(self) -> typing.List[Player]:
        return [mafia_pb2.PlayerDescription(name=x.name, is_ready=x.is_ready) for x in self.players.values()]
    
    def start_game(self) -> None:
        self.game = Game(self.game_size, self.players.values())

        for player in self.players.values():
            player.notifications.put(mafia_pb2.Notification(game_staet=self.game.make_state(), is_game_in_progress=True))


