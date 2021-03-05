import string


class CCipher:
    def decode(self, cipherText, shift):
        return "".join(
            map(
                lambda c: string.ascii_uppercase[(ord(c) - shift - ord("A")) % 26],
                cipherText,
            )
        )
