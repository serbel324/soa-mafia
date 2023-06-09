import grpc
from token_generator import generate_token
import auth_pb2_grpc
import auth_pb2

import typing
import logging

PLAYER_TOKEN_LENGTH = 32
PLAYER_TOKEN_CHARS = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'

class User():
    login: str = None
    password: str = None
    token: str = None

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self.token = generate_token(PLAYER_TOKEN_LENGTH, PLAYER_TOKEN_CHARS)


    def get_token(self, password: str) -> str:
        if password == self.password:
            return self.token
        else:
            return None


class AuthServerServicer(auth_pb2_grpc.AuthServerServicer):
    users: typing.Dict[str, User] = {}

    def Register(self, request, context):
        print("reg")
        login = request.login
        password = request.password

        if login in self.users.keys():
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            print(f'[auth] Registration failure: user with login \"{login}\" already exists') 
            raise ValueError('User with given login already exists')

        print(f'[auth] Registration successful: user with login \"{login}\" added')
        self.users[login] = User(login, password)
        return auth_pb2.RegisterResponse(token=self.users[login].token)


    def LogIn(self, request, context):
        print("lin")
        login = request.login
        password = request.password

        user = self.users.get(login, None)

        if user is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            print(f'[auth] Log in failure: user with login \"{login}\" doesn\'t exist')
            raise ValueError('User not found')

        if user.password != password:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            print(f'[auth] Log in failure: user with login \"{login}\" has sent wrong password')
            raise ValueError('Wrong password')

        print(f'[auth] Log in successful for user \"{login}\"')
        return auth_pb2.LogInResponse(token=user.token)
