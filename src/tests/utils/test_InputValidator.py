from src.main.backend.utils.InputValidator import InputValidator
from src.main.backend.exceptions.InputError import InputParsingError

import unittest
import os


class TestInputValidator(unittest.TestCase):
    RESOURCES_PATH = os.path.join("src", "tests", "resources")

    def test_file_is_invalid_raises_error(self):
        invalid_file = os.path.join(self.RESOURCES_PATH, "invalid-file-1.txt")

        with self.assertRaises(InputParsingError, msg="input error") as error:
            validator = InputValidator()
            validator.validate(invalid_file)
