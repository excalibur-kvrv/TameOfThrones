from typing import Any


class Generator:
    """ A class to abstract data printing/redirection/custom handling
    """

    @staticmethod
    def generate(input_data: Any, generator: Any):
        """
        :param input_data: The input data on which we need to produce some output.
        :param generator: A generator class to specify how to process the output.
        """

        generator.generate(input_data)
