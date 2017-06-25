import json
import RPi.GPIO as IO
import copy
from multiprocessing import Process
from . import input_pins, output_pins
from time import sleep
from . import utils




demo_array = [
    '000000000000000111111000000000000000000000000000000000000000000000000000000000000',
    '000000000000111000000111000000000000000000000000000000000000000000000000000000000',
    '000000000011000000000000110000000000000000000000000000000000000000000000000000000',
    '000000000100000000000000001000000000000000001111110000000000000000000000000000000',
    '000000001000000000000000000100000000000000110000001100000000000000000000000000000',
    '000000110000000000000000000011000000000001000000000010000000000111111000000000000',
    '000111000000000000000000000000111000000110000000000001100000011000000110000000000',
    '111000000000000000000000000000000111111000000000000000011111100000000001111111111',
]


class Drawer:
    def __init__(self):
        self.process = None

    def run_demo(self):
        self.start_drawing_process(self.get_new_args("demo", None))

    def start_drawing_process(self, kwargs):
        if self.process:
            print("Shutting old process...", end="")
            self.process.terminate()
            self.process.join()
            print("Done")

        print("Starting new proces... ", end="")
        self.process = Process(
            target=self.draw_continuous_array,
            kwargs=kwargs
        )
        self.process.start()
        print("Done")

    def draw_array(self, current_array):
        for output_pin, row in zip(output_pins, current_array):
            for input_pin, value in zip(input_pins, row):
                IO.output(input_pin, int(value) == 1)
            IO.output(output_pin, 0)
            sleep(0.00001)
            IO.output(output_pin, 1)


    def draw_continuous_array(self, array, iterations, move):
        while True:
            partial_view = [item[:8] for item in array]
            for i in range(iterations):
                self.draw_array(partial_view)

            for i, row in enumerate(array):
                if move:
                    array[i] = row[1:] + row[0]

    def get_new_args(self, mode, data):
        if mode == 'demo':
            return {
                "array": demo_array,
                "move": True,
                "iterations": 16
            }

        elif mode == 'string':
            return {
                "array": utils.get_array_from_string(data.upper()),
                "move": True,
                "iterations": 32
            }

        elif mode == 'letter':
            return {
                "array": utils.letters[data.upper()],
                "move": False,
                "iterations": 1
            }

        elif mode == 'point':
            return {
                'array': utils.get_point_array(*data),
                "move": False,
                "iterations": 1
            }

    def handle_message(self, new_data):
        try:
            new_kwargs = self.get_new_args(**new_data)
            self.start_drawing_process(new_kwargs)
        except KeyError:
            print("received incorrect data combination. Got", new_data)
