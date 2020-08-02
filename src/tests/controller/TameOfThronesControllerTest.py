from src.main.backend.controller.TameOfThronesController import Controller

import unittest
import os
import re


class TestTameOfThronesController(unittest.TestCase):
    RESOURCES_PATH = os.path.join("src", "tests", "resources")

    def test_inputs_generate_correct_output(self):
        extract_number = re.compile(r"(\d+)")

        for file_name in os.listdir(self.RESOURCES_PATH):
            if file_name.startswith("input-file-"):
                file_path = os.path.join(self.RESOURCES_PATH, file_name)
                Controller.run(file_path, output_type="file")

                extracted_number = extract_number.findall(file_name)[0]
                expected_output_file = f"output-file-{extracted_number}.txt"
                actual_output_file = f"actual-input-file-{extracted_number}.txt"

                with open(os.path.join(self.RESOURCES_PATH, expected_output_file)) as expected:
                    expected_data = expected.read()

                with open(os.path.join(self.RESOURCES_PATH, actual_output_file)) as actual:
                    actual_data = actual.read()

                assert actual_data.strip() == expected_data.strip(), \
                    f"expected {expected_data.strip()} but got {actual_data.strip()}"

                os.unlink(os.path.join(self.RESOURCES_PATH, actual_output_file))

