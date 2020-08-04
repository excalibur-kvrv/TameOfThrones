from src.main.backend.utils.OutputGenerator import OutputGenerator, FileOutputGenerator, ConsoleOutputGenerator
from src.main.backend.utils.OutputFactory import OutputFactory

import unittest


class TestOutput(unittest.TestCase):
    def test_output_factory_returns_correct_instance(self):
        output_factory = OutputFactory()
        output_service = output_factory.get_output_generator("file")

        assert isinstance(output_service, OutputGenerator), \
            f"expected {output_service}, but found {OutputGenerator}"

        assert isinstance(output_service, FileOutputGenerator), \
            f"expected {output_service}, but found {FileOutputGenerator}"

        output_service = output_factory.get_output_generator("console")

        assert isinstance(output_service, ConsoleOutputGenerator), \
            f"expected {output_service}, but found {ConsoleOutputGenerator}"
