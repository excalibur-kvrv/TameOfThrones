from src.main.backend.globals.constants import RUN_VALIDATION
from src.main.backend.utils.InputValidator import InputValidator
from src.main.backend.utils.OutputFactory import OutputFactory

from typing import Any


class Controller:
    """ A Controller class to run the TameOfThrones backend.
    """
    OUTPUT_FACTORY = OutputFactory()
    INPUT_VALIDATOR = InputValidator()

    def run(self, input_data: Any, output_type: str) -> None:
        """
        :param input_data: The data on which the TameOfThrones backend will run.
        :param output_type: This is used to indicate the where the output needs to be generated.
        """

        generator = self.OUTPUT_FACTORY.get_output_generator(output_type)

        # An input validator to validate the input file
        if RUN_VALIDATION:
            self.INPUT_VALIDATOR.validate(input_data)

        generator.generate(input_data)
