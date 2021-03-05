class TxMsg:
    def getMessage(self, original):
        v = "aeiou"

        def encode(s):
            r = [
                e
                for i, e in enumerate(s)
                if e not in v and ((i == 0) or i > 0 and s[i - 1] in v)
            ]
            return "".join(r) if r else s

        return " ".join(map(encode, original.split()))
