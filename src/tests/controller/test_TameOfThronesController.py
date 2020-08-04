from src.main.backend.controller.TameOfThronesController import Controller
from src.main.backend.globals.constants import SAVE_PATH

import unittest
import os
import re


class TestTameOfThronesController(unittest.TestCase):
    RESOURCES_PATH = os.path.join("src", "tests", "resources")

    def test_inputs_generate_correct_output(self):
        extract_number = re.compile(r"(\d+)")
        controller = Controller()

        for file_name in os.listdir(self.RESOURCES_PATH):
            if file_name.startswith("input-file-"):
                file_path = os.path.join(self.RESOURCES_PATH, file_name)

                controller.run(file_path, "file")

                extracted_number = extract_number.findall(file_name)[0]
                expected_output_file = f"output-file-{extracted_number}.txt"
                actual_output_file = f"actual-input-file-{extracted_number}.txt"

                with open(os.path.join(self.RESOURCES_PATH, expected_output_file)) as expected:
                    expected_data = expected.read()

                with open(os.path.join(SAVE_PATH, actual_output_file)) as actual:
                    actual_data = actual.read()

                assert actual_data == expected_data, f"expected {expected_data} but got {actual_data}"

                os.unlink(os.path.join(SAVE_PATH, actual_output_file))
