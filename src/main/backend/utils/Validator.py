from src.main.backend.exceptions.InputError import InputValidatorNotImplemented
from typing import Any


class Validator:
    """ A class to abstract the input_data validation.
    """

    @staticmethod
    def validate(input_data: Any, validator: Any) -> None:
        """
        :param input_data: The input_data to be validated by the 'validator'
        :param validator: A custom Validator to validate the 'input_data'
        """

        if not validator:
            raise InputValidatorNotImplemented(f"{validator} class is not defined")

        validator.validate(input_data)
