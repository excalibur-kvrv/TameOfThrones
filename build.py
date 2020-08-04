from src.tests.controller.test_TameOfThronesController import TestTameOfThronesController
from src.tests.models.test_Models import TestModels
from src.tests.repositoryservices.test_RepositoryImpl import TestKingdomRepository
from src.tests.services.test_Services import TestSoutherosService
from src.tests.utils.test_Cryptography import TestCryptography
from src.tests.utils.test_Output import TestOutput
from src.tests.utils.test_InputValidator import TestInputValidator

import subprocess
import unittest
import platform
import argparse


def controller_test_suite(suite):
    suite.addTest(TestTameOfThronesController("test_inputs_generate_correct_output"))


def models_test_suite(suite):
    suite.addTest(TestModels("test_receive_messages"))


def repository_service_test_suite(suite):
    suite.addTest(TestKingdomRepository("test_deserialization"))


def service_test_suite(suite):
    suite.addTest(TestSoutherosService("test_southeros_find_all_allies"))


def cryptography_test_suite(suite):
    suite.addTest(TestCryptography("test_crypto_factory_returns_correct_instance"))
    suite.addTest(TestCryptography("test_seaser_algorithm"))


def output_generator_test_suite(suite):
    suite.addTest(TestOutput("test_output_factory_returns_correct_instance"))


def input_validator_test_suite(suite):
    suite.addTest(TestInputValidator("test_file_is_invalid_raises_error"))


def run_tests():
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()

    # Tests
    controller_test_suite(suite)
    models_test_suite(suite)
    repository_service_test_suite(suite)
    service_test_suite(suite)
    cryptography_test_suite(suite)
    output_generator_test_suite(suite)
    input_validator_test_suite(suite)

    runner.run(suite)


if __name__ == "__main__":
    """
    Run The file using `python build.py -h` to see usage instructions.
    """

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file_path", help="The absolute or relative path to input file")
    args = arg_parser.parse_args()
    input_file_path = args.file_path

    run_tests()

    if platform.system() == "Windows":
        subprocess.run(f"python -m geektrust {input_file_path}", shell=True)
    else:
        subprocess.run(f"python3 -m geektrust {input_file_path}", shell=True)
