from auth_service import AuthServerServicer
import auth_pb2_grpc

import logging
from concurrent import futures
import grpc
import os
def serve():
    host = os.environ['HOST']
    port = os.environ['PORT']
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    auth_pb2_grpc.add_AuthServerServicer_to_server(AuthServerServicer(), server)

    addr = f'{host}:{port}'
    print(f'Running server on {addr}')
    server.add_insecure_port(addr)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
