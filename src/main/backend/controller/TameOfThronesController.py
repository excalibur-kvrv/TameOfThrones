from src.main.backend.utils.Generator import Generator
from src.main.backend.utils.InputValidator import InputValidator
from src.main.backend.utils.OutputGenerator import ConsoleOutputGenerator, FileOutputGenerator
from src.main.backend.utils.Validator import Validator

from typing import Any


class Controller:
    """ A Controller class to run the TameOfThrones backend.
    """

    @staticmethod
    def run(input_data: Any, output_type: str) -> None:
        """
        :param input_data: The data on which the TameOfThrones backend will run.
        :param output_type: This is used to indicate the where the output needs to be generated.
        """

        generator = ConsoleOutputGenerator()
        if output_type == "file":
            generator = FileOutputGenerator()

        Validator.validate(input_data, InputValidator)
        Generator.generate(input_data, generator)
