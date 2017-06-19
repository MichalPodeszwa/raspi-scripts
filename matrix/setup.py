import RPi.GPIO as IO
from pins import input_pins, output_pins
from utils import reset_matrix

def initialize():
    IO.setmode(IO.BOARD)
    IO.setwarnings(False)
    for pin in input_pins:
        IO.setup(pin, IO.OUT)

    for pin in output_pins:
        IO.setup(pin, IO.OUT)

    reset_matrix()
