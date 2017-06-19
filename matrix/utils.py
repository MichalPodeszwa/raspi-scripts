import RPi.GPIO as IO
from pins import input_pins, output_pins
from letters import letters
from time import sleep


def reset_matrix():
    for pin in input_pins:
        IO.output(pin, 0)
    for pin in output_pins:
        IO.output(pin, 1)


def light_point(x, y):
    IO.output(input_pins[y], 1)
    IO.output(output_pins[x], 0)


def draw_array(current_array):
    for output_pin, row in zip(output_pins, current_array):
        for input_pin, value in zip(input_pins, row):
            IO.output(input_pin, int(value) == 1)
        IO.output(output_pin, 0)
        sleep(0.00001)
        IO.output(output_pin, 1)


def draw_letter(letter):
    letters_array = letters[letter]

    while True:
        draw_array(letters_array)


def get_array_from_string(string, letter_spacing=1, wrap_spacing=4):
    letters_array = [letters[letter] for letter in string]

    whole_view = []

    for row in zip(*letters_array):
        whole_row = ''
        for letter_row in row:
            whole_row += letter_row + '0' * letter_spacing
        whole_view.append(whole_row + '0' * wrap_spacing)

    return whole_view


def draw_string(string, reader=None, iterations=45):
    whole_view = get_array_from_string(string)
    draw_continuous_array(whole_view, iterations, reader)


def draw_continuous_array(array, iterations=16, reader=None):
    while True:
        partial_view = [item[:8] for item in array]
        for i in range(iterations):
            draw_array(partial_view)
        if reader and reader.poll():
            new_string = reader.recv()
            array = get_array_from_string(new_string)
        else:
            for i, row in enumerate(array):
                array[i] = row[1:] + row[0]
