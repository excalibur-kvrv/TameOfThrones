from src.main.backend.exceptions.InputError import InputParsingError
import re


class InputValidator:
    """ A class to define a custom input Validator
    """

    @staticmethod
    def validate(input_data_path: str) -> None:
        """
        :param input_data_path: The absolute/relative path to input file.
        :exception InputParsingError: Raised when input file is not valid.
        """

        file_line_pattern = re.compile(r"^\s*[a-z]+ [a-z\s]+$", re.IGNORECASE)

        with open(input_data_path) as input_file:
            for line in input_file:
                if not file_line_pattern.findall(line):
                    raise InputParsingError(f"Every line in the file must follow case insensitive "
                                            f"pattern '^[a-z]+ [a-z\\s]+$'")
