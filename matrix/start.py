import RPi.GPIO as IO
import multiprocessing
import atexit
from time import sleep
from listeners import start_bluetooth_listener, start_console_listener
import drawer
import utils
from pins import input_pins, output_pins
from utils import reset_matrix

def initialize():
    IO.setmode(IO.BOARD)
    IO.setwarnings(False)
    for pin in input_pins:
        IO.setup(pin, IO.OUT)

    for pin in output_pins:
        IO.setup(pin, IO.OUT)

    utils.reset_matrix()


atexit.register(utils.reset_matrix)
if __name__ == '__main__':
    initialize()
    r, w = multiprocessing.Pipe(duplex=False)
    p = multiprocessing.Process(target=drawer.drawer, args=(r,))
    p.start()
    start_bluetooth_listener(w)

    start_console_listener(w)
