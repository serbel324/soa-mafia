from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

Civilian: Role
DESCRIPTOR: _descriptor.FileDescriptor
Day: Phase
Mafia: Role
NightMafia: Phase
NightSheriff: Phase
Sheriff: Role

class Blame(_message.Message):
    __slots__ = ["target_name"]
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    def __init__(self, target_name: _Optional[str] = ...) -> None: ...

class CreateRoomRequest(_message.Message):
    __slots__ = ["comment", "game_size", "name"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    GAME_SIZE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    comment: str
    game_size: int
    name: str
    def __init__(self, name: _Optional[str] = ..., game_size: _Optional[int] = ..., comment: _Optional[str] = ...) -> None: ...

class CreateRoomResponse(_message.Message):
    __slots__ = ["admin_token"]
    ADMIN_TOKEN_FIELD_NUMBER: _ClassVar[int]
    admin_token: str
    def __init__(self, admin_token: _Optional[str] = ...) -> None: ...

class DeleteRoomRequest(_message.Message):
    __slots__ = ["admin_token", "room_name"]
    ADMIN_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    admin_token: str
    room_name: str
    def __init__(self, room_name: _Optional[str] = ..., admin_token: _Optional[str] = ...) -> None: ...

class GameActionRequest(_message.Message):
    __slots__ = ["blame", "player_token", "random_move", "room_name", "slay"]
    BLAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RANDOM_MOVE_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    SLAY_FIELD_NUMBER: _ClassVar[int]
    blame: Blame
    player_token: str
    random_move: RandomMove
    room_name: str
    slay: Slay
    def __init__(self, room_name: _Optional[str] = ..., player_token: _Optional[str] = ..., slay: _Optional[_Union[Slay, _Mapping]] = ..., blame: _Optional[_Union[Blame, _Mapping]] = ..., random_move: _Optional[_Union[RandomMove, _Mapping]] = ...) -> None: ...

class GameActionResponse(_message.Message):
    __slots__ = ["game_state", "success"]
    GAME_STATE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    game_state: GameState
    success: bool
    def __init__(self, success: bool = ..., game_state: _Optional[_Union[GameState, _Mapping]] = ...) -> None: ...

class GameState(_message.Message):
    __slots__ = ["phase", "players", "turn"]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    TURN_FIELD_NUMBER: _ClassVar[int]
    phase: Phase
    players: _containers.RepeatedCompositeFieldContainer[Player]
    turn: int
    def __init__(self, phase: _Optional[_Union[Phase, str]] = ..., players: _Optional[_Iterable[_Union[Player, _Mapping]]] = ..., turn: _Optional[int] = ...) -> None: ...

class GetPlayerListRequest(_message.Message):
    __slots__ = ["room_name"]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    room_name: str
    def __init__(self, room_name: _Optional[str] = ...) -> None: ...

class GetPlayerListResponse(_message.Message):
    __slots__ = ["players"]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[PlayerDescription]
    def __init__(self, players: _Optional[_Iterable[_Union[PlayerDescription, _Mapping]]] = ...) -> None: ...

class GetRoomListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetRoomListResponse(_message.Message):
    __slots__ = ["rooms"]
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    rooms: _containers.RepeatedCompositeFieldContainer[RoomDescription]
    def __init__(self, rooms: _Optional[_Iterable[_Union[RoomDescription, _Mapping]]] = ...) -> None: ...

class JoinRoomRequest(_message.Message):
    __slots__ = ["player_name", "player_token", "room_name"]
    PLAYER_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    player_name: str
    player_token: str
    room_name: str
    def __init__(self, room_name: _Optional[str] = ..., player_name: _Optional[str] = ..., player_token: _Optional[str] = ...) -> None: ...

class JoinRoomResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LeaveRoomRequest(_message.Message):
    __slots__ = ["player_token", "room_name"]
    PLAYER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    player_token: str
    room_name: str
    def __init__(self, room_name: _Optional[str] = ..., player_token: _Optional[str] = ...) -> None: ...

class Notification(_message.Message):
    __slots__ = ["game_state", "is_game_in_progress", "players"]
    GAME_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_GAME_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    game_state: GameState
    is_game_in_progress: bool
    players: _containers.RepeatedCompositeFieldContainer[PlayerDescription]
    def __init__(self, players: _Optional[_Iterable[_Union[PlayerDescription, _Mapping]]] = ..., game_state: _Optional[_Union[GameState, _Mapping]] = ..., is_game_in_progress: bool = ...) -> None: ...

class Player(_message.Message):
    __slots__ = ["is_alive", "name", "role", "votes_for"]
    IS_ALIVE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    VOTES_FOR_FIELD_NUMBER: _ClassVar[int]
    is_alive: bool
    name: str
    role: Role
    votes_for: int
    def __init__(self, name: _Optional[str] = ..., votes_for: _Optional[int] = ..., role: _Optional[_Union[Role, str]] = ..., is_alive: bool = ...) -> None: ...

class PlayerDescription(_message.Message):
    __slots__ = ["is_ready", "name"]
    IS_READY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    is_ready: bool
    name: str
    def __init__(self, name: _Optional[str] = ..., is_ready: bool = ...) -> None: ...

class RandomMove(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RoomDescription(_message.Message):
    __slots__ = ["comment", "game_size", "name", "num_players"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    GAME_SIZE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    comment: str
    game_size: int
    name: str
    num_players: int
    def __init__(self, name: _Optional[str] = ..., comment: _Optional[str] = ..., num_players: _Optional[int] = ..., game_size: _Optional[int] = ...) -> None: ...

class SignalIsReadyRequest(_message.Message):
    __slots__ = ["player_token", "room_name"]
    PLAYER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    player_token: str
    room_name: str
    def __init__(self, room_name: _Optional[str] = ..., player_token: _Optional[str] = ...) -> None: ...

class Slay(_message.Message):
    __slots__ = ["target_name"]
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    def __init__(self, target_name: _Optional[str] = ...) -> None: ...

class SubscribeOnNotificationsRequest(_message.Message):
    __slots__ = ["player_token", "room_name"]
    PLAYER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    player_token: str
    room_name: str
    def __init__(self, room_name: _Optional[str] = ..., player_token: _Optional[str] = ...) -> None: ...

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Phase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
