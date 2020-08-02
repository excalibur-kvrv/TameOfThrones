from src.main.backend.controller.TameOfThronesController import Controller

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

    Controller.run(input_file, output_type="console")


if __name__ == "__main__":
    main()
