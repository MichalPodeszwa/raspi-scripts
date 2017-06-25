import os
import socket
import json
import sys
from functools import wraps

from config import server_address


def handle_socket_file(f):
    @wraps(f)
    def _wrapper(*args, **kwargs):
        print("Ensuring socket doesn't exist")
        if os.path.exists(server_address):
            print("Removing old socket")
            os.remove(server_address)

        f(*args, **kwargs)

        print("Cleaning up after socket")
        os.remove(server_address)

    return _wrapper


def create_socket(f):
    @wraps(f)
    def _wrapper(*args, **kwargs):
        print("Opening socket...", end="")
        server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        server.bind(server_address)
        print("Done")

        f(*args, server=server, **kwargs)

        server.close()
    return _wrapper

def parse_data(data):
    data = data.decode()
    try:
        data = json.loads(data)
    except ValueError:
        print("Received incorrect data", data, file=sys.stderr)
    else:
        return data

def is_data_correct(data):
    if "mode" not in data or "data" not in data:
        print("\"mode\" and \"data\" is required in received data. Got", data)
        return False
    else:
        return True


@handle_socket_file
@create_socket
def start_server(callback, *, server):
    print("Listening on", server_address)

    while True:
        data = server.recv(1024)
        if not data:
            break
        else:
            data = parse_data(data)
            if is_data_correct(data):
                callback(data)
