import string
import random
import secrets


class Password:
    DIGITS = 1
    STRINGS = 2
    ALPHABET = 3
    ALL = 4

    def __generate_digits(self, length):
        return random.choices(string.digits, k=length)

    def __generate_strings(self, length):
        return random.choices(string.ascii_letters, k=length)

    def __generate_alphabet(self, length):
        length_digits = round(length*0.2)
        digits = self.__generate_digits(length_digits)
        s = self.__generate_strings(length-length_digits)
        merge = digits + s
        random.shuffle(merge)
        return merge

    def __generate_all(self, length):
        punctuation = random.choices(string.punctuation)
        pwd = self.__generate_alphabet(length)
        merge = punctuation + pwd
        random.shuffle(merge)
        return merge

    def generate(self, length, sort):
        if sort == Password.DIGITS:
            return ''.join(x for x in self.__generate_digits(length))
        elif sort == Password.STRINGS:
            return ''.join(x for x in self.__generate_strings(length))
        elif sort == Password.ALPHABET:
            return ''.join(x for x in self.__generate_alphabet(length))
        elif sort == Password.ALL:
            return ''.join(x for x in self.__generate_all(length))
        else:
            return None

    def generate_token(self):
        return secrets.token_urlsafe()
