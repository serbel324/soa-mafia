from mafia_service import MafiaServerServicer
import mafia_pb2_grpc

import logging
import grpc
from concurrent import futures
import os

def serve():
    host = os.environ['HOST']
    port = os.environ['PORT']
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mafia_pb2_grpc.add_MafiaServerServicer_to_server(MafiaServerServicer(), server)

    addr = f'{host}:{port}'
    print(f'Running server on {addr}')
    server.add_insecure_port(addr)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()