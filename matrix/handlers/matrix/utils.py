import RPi.GPIO as IO
from time import sleep
import functools

from . import input_pins, output_pins
from .letters import letters

def reset_matrix():
    for pin in input_pins:
        IO.output(pin, 0)
    for pin in output_pins:
        IO.output(pin, 1)


def get_point_array(x, y):
    array = [[0] * 8 for _ in range(8)]
    array[y][x] = 1
    return array


def get_array_from_string(string, letter_spacing=1, wrap_spacing=4):
    letters_array = [letters[letter] for letter in string]

    whole_view = []

    for row in zip(*letters_array):
        whole_row = ''
        for letter_row in row:
            whole_row += letter_row + '0' * letter_spacing
        whole_view.append(whole_row + '0' * wrap_spacing)

    return whole_view
