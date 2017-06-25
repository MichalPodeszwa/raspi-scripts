from config import server_address, bluetooth_uuid
from listeners.common import get_socket
import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    data = request.get_json()

    client_sock = get_socket()
    client_sock.send(json.dumps(data))

    return "Sent"

def start_listener():
    app.run("0.0.0.0", 8000)
