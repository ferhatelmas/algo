from string import ascii_lowercase

class TwoRotationCypher:
    def encrypt(self, firstSize, firstRotate, secondRotate, message):
        f, s, r = ascii_lowercase[:firstSize], ascii_lowercase[firstSize:], ''
        for e in message:
            if e == ' ':
                r += e
            elif e in f:
                r += chr(ord(f[0]) + (ord(e) - ord(f[0]) + firstRotate)%firstSize)
            else:
                r += chr(ord(s[0]) + (ord(e) - ord(s[0]) + secondRotate)%(26-firstSize))
        return r
