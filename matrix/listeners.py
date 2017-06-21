import multiprocessing
from bluetooth import *


def bluetooth_listener(write_pipe):
    server_sock = BluetoothSocket(RFCOMM)
    server_sock.bind(("", PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    advertise_service(
        server_sock,
        "SampleServer",
        service_id=uuid,
        service_classes=[uuid, SERIAL_PORT_CLASS],
        profiles=[SERIAL_PORT_PROFILE],
    )

    client_sock, client_info = server_sock.accept()

    while True:
        data = client_sock.recv(1024)
        if len(data) == 0:
            break
        write_pipe.send(data.decode())


def start_bluetooth_listener(write_pipe):
    print("Starting Bluetooth listener... ", end="")
    p = multiprocessing.Process(target=bluetooth_listener, args=(write_pipe,))
    p.start()
    print("Started")
    return p


def start_console_listener(write_pipe):
    while True:
        new_string = input("Type anything to change to new string...\t")
        write_pipe.send(new_string)
