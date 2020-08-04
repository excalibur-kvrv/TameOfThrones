from src.main.backend.exceptions.InputError import InputParsingError
from src.main.backend.globals.constants import FILE_PATTERN
import re


class InputValidator:
    """ A class to define a custom input Validator
    """

    def validate(self, input_data_path: str) -> None:
        """
        :param input_data_path: The absolute/relative path to input file.
        :exception InputParsingError: Raised when input file is not valid.
        """

        file_line_pattern = re.compile(FILE_PATTERN, re.IGNORECASE)

        with open(input_data_path) as input_file:
            for line in input_file:
                if not file_line_pattern.findall(line):
                    raise InputParsingError(f"Input file not matching provided pattern. {FILE_PATTERN}")
