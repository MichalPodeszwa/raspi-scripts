from bluetooth import *
from config import server_address, bluetooth_uuid
from listeners.common import get_socket
import json

def start_listener():
    print("Starting bluetooth server... ", end="")
    server_sock = BluetoothSocket(RFCOMM)
    server_sock.bind(("", PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    advertise_service(
        server_sock,
        "SampleServer",
        service_id=bluetooth_uuid,
        service_classes=[bluetooth_uuid, SERIAL_PORT_CLASS],
        profiles=[SERIAL_PORT_PROFILE],
    )

    print("Done")
    client_socket, client_info = server_sock.accept()
    while True:
        data = client_socket.recv(1024)
        if len(data) == 0:
            break

        client_sock = get_socket()
        client_sock.send(data)
