import re

class VowelEncryptor:
    def encrypt(self, text):
        vs = set('aeiou')
        def enc(s):
            if set(s) - vs:
                return re.sub(r'[aeiou]', '', s)
            return s
        return map(enc, text)
