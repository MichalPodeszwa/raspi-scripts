import json
import sys
from contextlib import suppress

class SocketWrapper():
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        if isinstance(data, bytes):
            data = data.decode()

        try:
            data = json.loads(data)
        except ValueError:
            print("Got invalid data", data, file=sys.stderr)
        else:
            self.socket.send(json.dumps(data).encode())
