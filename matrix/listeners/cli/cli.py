import click
from listeners.common import get_socket

def send_data(data):
    socket = get_socket()
    socket.send(data)

@click.group()
def cli():
    pass

@cli.command()
@click.argument("value")
def string(value):
    send_data({
        "mode": "string",
        "data": value
    })

@cli.command()
def demo():
    send_data({
        "mode": "demo",
        "data": ""
    })

@cli.command()
@click.argument("letter")
def letter(letter):
    send_data({
        "mode": "letter",
        "data": letter[0]
    })
