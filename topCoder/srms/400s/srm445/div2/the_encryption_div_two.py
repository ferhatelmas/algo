from string import ascii_lowercase

class TheEncryptionDivTwo:
    def encrypt(self, message):
        i, d, s = 0, {}, []
        for e in message:
            if e not in d:
                d[e] = ascii_lowercase[i]
                i += 1
            s.append(d[e])
        return ''.join(s)
