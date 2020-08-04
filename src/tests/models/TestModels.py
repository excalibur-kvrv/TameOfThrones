from src.main.backend.utils.CryptographyFactory import CryptographyFactory
from src.main.backend.models.Kingdom import Kingdom

import unittest


class TestModels(unittest.TestCase):
    def test_receive_messages(self):
        crypto_factory = CryptographyFactory()
        crypto_service = crypto_factory.get_cryptographic_strategy("seaser")
        kingdom = Kingdom("AIR", "OWL", crypto_service)

        assert kingdom.receive_message("OWLAOWLBOWLC") is False, \
            f"expected False, but Got True"
        assert kingdom.receive_message("RIZI") is False, \
            f"expected False but Got True"
        assert kingdom.receive_message("ROZO") is True, \
            f"expected True but Got False"
