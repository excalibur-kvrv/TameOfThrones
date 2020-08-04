from src.main.backend.utils.CryptographyFactory import CryptographyFactory
from src.main.backend.utils.Cryptography import Cryptography
from src.main.backend.utils.SeasarCipher import SeaserCipher

import unittest


class TestCryptography(unittest.TestCase):
    def test_crypto_factory_returns_correct_instance(self):
        crypto_factory = CryptographyFactory()
        crypto_service = crypto_factory.get_cryptographic_strategy("seaser")

        assert isinstance(crypto_service, Cryptography), f"expected {Cryptography}, but found {crypto_service}"
        assert isinstance(crypto_service, SeaserCipher), f"expected {SeaserCipher}, but found {crypto_service}"

    def test_seaser_algorithm(self):
        seaser = SeaserCipher()
        seaser.first_char = ord("A")
        seaser.last_char = ord("A") + 26

        ciphers_encrypt_decrypt = [
            ("X", "W", 1),
            ("XA", "WZ", 1),
            ("XYZABC", "TUVWXY", 4)
        ]

        for encrypted_text, decrypted_text, cipher_key in ciphers_encrypt_decrypt:
            result = seaser.decrypt(encrypted_text, cipher_key)
            assert result == decrypted_text, f"expected {decrypted_text}, but got {result}"
