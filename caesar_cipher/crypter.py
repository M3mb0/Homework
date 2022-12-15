"""This modul contain 2 classes for encrypting and decrypting a text in 2 ways"""


class Caesar:
    """Generate new alphabet shifted by key"""

    def __init__(self, key):
        self.__key = key

    def crypt(self, message):
        """Crypt the message and return it"""
        encrypted_msg = "Caesar\n" + ""
        for char in message:
            if char == " ":
                encrypted_msg += " "
                continue
            if any(letter.isupper() for letter in char):
                encrypted_msg += chr((ord(char) + self.__key - 65) % 26 + 65)
            elif any(letter.islower() for letter in char):
                encrypted_msg += chr((ord(char) + self.__key - 97) % 26 + 97)
            else:
                encrypted_msg += char
        return encrypted_msg

    def decrypt(self, message):
        """Decrypt the message and return it."""
        decrypted_msg = ""
        for char in message:
            if char == " ":
                decrypted_msg += " "
                continue
            if any(letter.isupper() for letter in char):
                decrypted_msg += chr((ord(char) - self.__key - 65) % 26 + 65)
            elif any(letter.islower() for letter in char):
                decrypted_msg += chr((ord(char) - self.__key - 97) % 26 + 97)
            else:
                decrypted_msg += char
        return decrypted_msg


class Shift:
    """Move letters in words by key"""

    def __init__(self, key):
        self.__key = key

    def crypt(self, message):
        """Crypt the message and return it"""
        encrypted_msg = "Shift\n" + ""
        for word in message.split():
            if len(word) <= 1:
                encrypted_msg += word + ' '
            elif len(word) < self.__key:
                if (self.__key % len(word)) != 0:
                    if word[0].isupper():
                        encrypted_msg += word[-(self.__key % len(word)):].capitalize() + word[0:(
                                len(word) - (self.__key % len(word)))].lower() + ' '
                    else:
                        encrypted_msg += word[-(self.__key % len(word)):] + word[0:(
                                len(word) - (self.__key % len(word)))] + ' '
                else:
                    if word[0].isupper():
                        encrypted_msg += word[::-1].capitalize() + ' '
                    else:
                        encrypted_msg += word[::-1] + ' '
            elif len(word) == self.__key:
                if word[0].isupper():
                    encrypted_msg += word[::-1].capitalize() + ' '
                else:
                    encrypted_msg += word[::-1] + ' '
            else:
                if word[0].isupper():
                    encrypted_msg += word[-self.__key:].capitalize() + word[0:-self.__key].lower() + ' '
                else:
                    encrypted_msg += word[-self.__key:] + word[0:-self.__key] + ' '
        return encrypted_msg

    def decrypt(self, message):
        """Decrypt the message and return it."""
        encrypted_msg = ""
        for word in message.split():
            if len(word) <= 1:
                encrypted_msg += word + ' '
            elif len(word) < self.__key:
                if (self.__key % len(word)) != 0:
                    if word[0].isupper():
                        encrypted_msg += word[self.__key % len(word) - len(word):].capitalize() + word[0:(
                                len(word) + self.__key % len(word) - len(word))].lower() + ' '
                    else:
                        encrypted_msg += word[self.__key % len(word) - len(word):] + word[0:(
                                len(word) + self.__key % len(word) - len(word))] + ' '
                else:
                    if word[0].isupper():
                        encrypted_msg += word[::-1].capitalize() + ' '
                    else:
                        encrypted_msg += word[::-1] + ' '
            elif len(word) == self.__key:
                if word[0].isupper():
                    encrypted_msg += word[::-1].capitalize() + ' '
                else:
                    encrypted_msg += word[::-1] + ' '
            else:
                if word[0].isupper():
                    encrypted_msg += word[self.__key - len(word):].capitalize() + word[0:self.__key - len(
                        word)].lower() + ' '
                else:
                    encrypted_msg += word[self.__key - len(word):] + word[0:self.__key - len(word)] + ' '
        return encrypted_msg
