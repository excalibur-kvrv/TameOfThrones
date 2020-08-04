from src.main.backend.controller.TameOfThronesController import Controller
from src.main.backend.globals.constants import OUTPUT_TYPE

import sys
import os


def main():
    """ The main method takes a command line argument as parameter, which points to a input file to run,
        the Tame Of Thrones backend.

    :exception FileNotFoundError: This is raised when command line argument does not point to a file.
    """

    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"{input_file} is not a valid path")

    tame_of_thrones_controller = Controller()
    tame_of_thrones_controller.run(input_file, OUTPUT_TYPE)


if __name__ == "__main__":
    main()
