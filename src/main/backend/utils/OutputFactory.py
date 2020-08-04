from src.main.backend.utils.OutputGenerator import FileOutputGenerator, ConsoleOutputGenerator, OutputGenerator


class OutputFactory:
    """ A factory class to create Output Generator objects.
    """

    def get_output_generator(self, output_type: str) -> OutputGenerator:
        """
        get_cryptographic_strategy() -> This is a factory method to create Cryptography objects.
        :param output_type: This is used to generate the output.
        :exception NotImplementedError: raised when strategy of type Cryptography is not available.
        :return: An object of type Cryptography.
        """

        if output_type.lower() == "console":
            return ConsoleOutputGenerator()

        if output_type.lower() == "file":
            return FileOutputGenerator()

        raise NotImplementedError(f"Output of type {output_type} is not implemented.")
