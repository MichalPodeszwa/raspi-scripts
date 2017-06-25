import socket
import os
import sys
from config import server_address
from .SocketWrapper import SocketWrapper


def get_socket():
    print("Establishing connection to:", server_address)
    if not os.path.exists(server_address):
        print("Server", server_address, "doesn't exist", file=sys.stderr)
        raise Exception("Server does not exist!")

    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect(server_address)
    print("Connected")
    return SocketWrapper(client)
