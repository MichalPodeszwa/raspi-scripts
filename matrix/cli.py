import click
import utils
import multiprocessing
from setup import initialize
import atexit
from time import sleep

@click.group()
def cli():
    pass

@cli.command()
def reset():
    utils.reset_matrix()

@cli.command()
@click.argument('letter')
def letter(letter):
    utils.draw_letter(letter)

@cli.command()
@click.argument('string')
def string(string):
    utils.draw_string(string)

@cli.command()
def demo():
    utils.draw_continuous_array([
        '000000000000000111111000000000000000000000000000000000000000000000000000000000000',
        '000000000000111000000111000000000000000000000000000000000000000000000000000000000',
        '000000000011000000000000110000000000000000000000000000000000000000000000000000000',
        '000000000100000000000000001000000000000000001111110000000000000000000000000000000',
        '000000001000000000000000000100000000000000110000001100000000000000000000000000000',
        '000000110000000000000000000011000000000001000000000010000000000111111000000000000',
        '000111000000000000000000000000111000000110000000000001100000011000000110000000000',
        '111000000000000000000000000000000111111000000000000000011111100000000001111111111',
    ])

@cli.command()
def start():
    r, w = multiprocessing.Pipe(duplex=False)
    p = multiprocessing.Process(target=utils.draw_string, args=("WAITING", r))
    p.start()
    while True:
        new_string = input("Type anything to change to new string...\t")
        w.send(new_string)

atexit.register(utils.reset_matrix)

if __name__ == '__main__':
    initialize()
    cli()
