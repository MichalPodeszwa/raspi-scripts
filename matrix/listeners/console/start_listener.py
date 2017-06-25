from listeners.common import get_socket

def start_listener():

    while True:
        new_string = input("Type anything to change to new string...\t")
        client_sock = get_socket()
        client_sock.send(new_string)
