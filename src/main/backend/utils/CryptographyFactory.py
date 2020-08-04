from src.main.backend.utils.Cryptography import Cryptography
from src.main.backend.utils.SeasarCipher import SeaserCipher


class CryptographyFactory:
    """ A factory class to create Cryptography objects.
    """

    def get_cryptographic_strategy(self, strategy: str) -> Cryptography:
        """
        get_cryptographic_strategy() -> This is a factory method to create Cryptography objects.
        :param strategy: The cryptographic strategy to implement.
        :exception NotImplementedError: raised when strategy of type Cryptography is not available.
        :return: An object of type Cryptography.
        """

        if strategy.lower() == "seaser":
            return SeaserCipher()

        raise NotImplementedError(f"Strategy of type {strategy} is not implemented.")
