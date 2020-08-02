from src.main.backend.models.Kingdom import Kingdom
from typing import List


class Ruler(Kingdom):
    """ A class to model a ruler.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__allies = list()

    def add_ally(self, ally: Kingdom):
        self.__allies.append(ally)

    def get_allies(self) -> List[Kingdom]:
        return self.__allies

    def send_message(self, message: str, kingdom_emblem: str) -> str:
        """
        send_message() -> This method sends the encrypted message to a kingdom.
        :param message: The message to be encrypted.
        :param kingdom_emblem: The kingdom_emblem of the kingdom that receives the message.
        :return: A string representing the encrypted message.
        """

        crypto_strategy = self.get_crypto_strategy()
        cipher_key = len(kingdom_emblem)
        encrypted_message = crypto_strategy.encrypt(message, cipher_key)

        return encrypted_message
