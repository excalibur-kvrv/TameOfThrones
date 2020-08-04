from src.main.backend.services.SoutherosRulerServiceImpl import SoutherosRulerServiceImpl
from src.main.backend.utils.OutputFactory import OutputFactory

import unittest
import os


class TestSoutherosService(unittest.TestCase):
    RESOURCE_PATH = os.path.join("src", "tests", "resources")
    RULER_SERVICE = SoutherosRulerServiceImpl()

    def test_southeros_find_all_allies(self):
        file_path = os.path.join(self.RESOURCE_PATH, "input-file-1.txt")

        output_factory = OutputFactory()
        generator = output_factory.get_output_generator("file")
        file_mappings = generator.read_file(file_path)

        result = self.RULER_SERVICE.find_all_allies_for_rulers(file_mappings)

        assert result[0].get_name() == "SPACE"
        assert len(result[0].get_allies()) == 3
