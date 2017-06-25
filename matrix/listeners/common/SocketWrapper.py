import json
import sys
from contextlib import suppress

class SocketWrapper():
    def __init__(self, socket):
        self.socket = socket

    def ensure_data_is_dict(self, data):
        if isinstance(data, bytes):
            data = data.decode()

        if isinstance(data, str):
            try:
                data = json.loads(data)
            except ValueError:
                print("Got invalid data", data, file=sys.stderr)

        if not isinstance(data, dict):
            print("Something went wrong. Expected data to be dict but is not. Data =", data)
            return None

        return data


    def send(self, data):
        data = self.ensure_data_is_dict(data)

        if data:
            self.socket.send(json.dumps(data).encode())
