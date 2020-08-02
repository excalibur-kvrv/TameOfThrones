from src.main.backend.utils.Cryptography import Cryptography


class SeaserCipher(Cryptography):
    def encrypt(self, message: str, key: int) -> str:
        return message

    def decrypt(self, message: str, key: int) -> str:
        """
        :param message: The message to be decrypted using key.
        :param key: The key to be used to decrypt the message.
        :return: decrypted message using key.
        """

        decrypted_message_chunks = []

        for letter in message.lower():

            char_val = ord(letter) - key

            if char_val < 97:
                decrypted_chunk = chr(((123 - (97 - char_val)) % 97) + 97)
            else:
                decrypted_chunk = chr((char_val % 97) + 97)

            decrypted_message_chunks.append(decrypted_chunk)

        return "".join(decrypted_message_chunks)
