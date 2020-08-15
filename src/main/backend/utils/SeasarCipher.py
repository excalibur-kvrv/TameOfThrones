from src.main.backend.globals.constants import FIRST_CHAR_UNICODE_VALUE, LAST_CHAR_UNICODE_VALUE
from src.main.backend.utils.Cryptography import Cryptography


class SeaserCipher(Cryptography):
    def __init__(self):
        self.first_char = FIRST_CHAR_UNICODE_VALUE
        self.last_char = LAST_CHAR_UNICODE_VALUE

    def encrypt(self, message: str, key: int) -> str:
        return message

    def decrypt(self, message: str, key: int) -> str:
        """
        :param message: The message to be decrypted using key.
        :param key: The key to be used to decrypt the message.
        :return: decrypted message using key.
        """

        decrypted_message_chunks = []

        for char in message:
            char = self.__validate_character(char)
            char_val = ord(char) - key

            if char_val < self.first_char:
                decrypted_chunk = chr(((self.last_char - (self.first_char - char_val))
                                       % self.first_char) + self.first_char)
            else:
                decrypted_chunk = chr((char_val % self.first_char) + self.first_char)

            decrypted_message_chunks.append(decrypted_chunk)

        return "".join(decrypted_message_chunks)

    def __validate_character(self, char):
        if self.first_char == ord("A") and char.islower():
            return char.upper()
        elif self.first_char == ord("a") and char.isupper():
            return char.lower()
        return char
