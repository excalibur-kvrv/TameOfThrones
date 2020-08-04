from src.main.backend.utils.Cryptography import Cryptography
from collections import Counter


class Kingdom:
    """ A class to model a Kingdom
    """

    def __init__(self, name: str, emblem: str, cryptographic_strategy: Cryptography):
        """
        :param name: The name of the kingdom
        :param emblem: The emblem unique to the Kingdom.
        :param cryptographic_strategy: The strategy to be used for message passing between kingdoms.
        """

        self.__name = name
        self.__emblem = emblem
        self.__crypto_strategy = cryptographic_strategy

    def get_emblem(self) -> str:
        return self.__emblem

    def get_crypto_strategy(self) -> Cryptography:
        return self.__crypto_strategy

    def get_name(self) -> str:
        return self.__name

    def receive_message(self, message: str) -> bool:
        """
        receive_message() -> This method is used to indicate whether kingdom will ally itself with a ruler.
        :param message: The encrypted message.
        :return: a boolean indicating the kingdom's stance on allying itself with a ruler.
        """

        crypto_strategy = self.get_crypto_strategy()
        cipher_key = len(self.get_emblem())
        decrypted_message = crypto_strategy.decrypt(message, cipher_key)

        return self.__will_ally(decrypted_message)

    def __will_ally(self, message: str) -> bool:
        """
        __will_ally() -> A kingdom allies with a ruler if the message contains all the letters of the kingdom.
        :param message: The message to be checked for alliance.
        :return: a boolean indicating if the kingdom's emblem was found in the message.
        """

        cipher_message = Counter(message)
        emblem_char_frequency = Counter(self.get_emblem())

        for letter, frequency in emblem_char_frequency.items():
            if letter not in cipher_message or cipher_message[letter] < frequency:
                return False

        return True

    def __repr__(self):
        return self.get_name()
