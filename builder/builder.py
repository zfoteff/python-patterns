__author__ = "Zac Foteff"
__version__ = "v1.0.0"

import sys
from operator import ge
from random import randint

class PasswordBuilder:
    """Builds a password according to user specifications. The builder
    will allow the user to specify the length of the password and the
    inclusion of
    * Uppercase characters
    * Lowercase characters
    * Special characters
    * Digits
    * Unsafe special characters
    Default passwords are a mix of 8 lower & uppercase letters
    """

    _MAX_LENGTH = 25

    def __init__(self):
        self.__valid_characters = list()

    def build(self, length: int = 8, number_to_generate: int = 1) -> list:
        """Build a password based off of the inputted settings for the builder.
        Should check that 0 <= length <= 25 and 1 <= number_to_generate <= 50. Defaults
        to generating a password with only upper and lowercase letters

        Args:
            length (int, optional): Length of the password strings to generate. Defaults to 8.
            number_to_generate (int, optional): Number of passwords that should be outputted. Defaults to 1.

        Returns:
            _type_: _description_
        """
        if length <= 0:
            length = 8
        elif length > self._MAX_LENGTH:
            length = self._MAX_LENGTH
        elif self.__valid_characters == [] or self.__valid_characters is None:
            self.uppercase().lowercase()

        generated_passwords = []
        for _ in range(0, number_to_generate):
            generated_password = ""
            for _ in range(0, length):
                generated_password += self.__valid_characters[
                    randint(0, len(self.__valid_characters))
                ]
            generated_passwords.append(generated_password)

        return generated_passwords

    def uppercase(self, include_uppercase: bool = True):
        """_summary_

        Args:
            include_uppercase (bool, optional): _description_. Defaults to True.
        Returns:
            _type_: _description_
        """
        if include_uppercase:
            uppercase = [chr(letter) for letter in range(65, 91)]
            self.__valid_characters += uppercase
        return self

    def lowercase(self, include_lowercase: bool = True):
        if include_lowercase:
            lowercase = [chr(letter) for letter in range(97, 123)]
            self.__valid_characters += lowercase
        return self

    def digits(self, include_digits: bool = True):
        if include_digits:
            digits = [str(digit) for digit in range(0, 10)]
            print(digits)
            self.__valid_characters += digits
        return self

    def symbols(self, include_symbols: bool = True):
        if include_symbols:
            symbols = [
                ".",
                ",",
                ":",
                ";",
                "[",
                "]",
                "(",
                ")",
                "'",
                "~",
                "-",
                "_",
                "+",
                "=",
                "{",
                "}",
                "|",
                "<",
                ">",
                "/",
                "?",
                "!",
                "#",
                "$",
                "%",
                "&",
                "*",
            ]
            print(symbols)
            self.__valid_characters += symbols
        return self

    def unsafe_symbols(self, include_unsafe_symbols: bool = True):
        if include_unsafe_symbols:
            unsafe_symbols = ["\\", "@", '"', "`", "^"]
            print(unsafe_symbols)
            self.__valid_characters += unsafe_symbols
        return self


if __name__ == "__main__":
    builder = PasswordBuilder().build()
    for password in builder:
        print(password)
