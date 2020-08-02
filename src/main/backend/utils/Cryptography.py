from typing import Any
import abc


class Cryptography(metaclass=abc.ABCMeta):
    """ An interface to interact with cryptographic algorithms
    """

    @abc.abstractmethod
    def encrypt(self, message: str, key: Any) -> str:
        """
        encrypt() -> This function is used to encrypt messages using the provided key.
        :param message: The message to encrypt using 'key'.
        :param key: The key to be used to encrypt 'message'.
        :return: The encrypted message.
        """

        pass

    @abc.abstractmethod
    def decrypt(self, message: str, key: Any) -> str:
        """
        decrypt() -> This function is used to decrypt messages using the provided key.
        :param message: The encrypted message to be decrypted.
        :param key: The key using which we decrypted the encrypted message.
        :return: The decrypted message.
        """

        pass
