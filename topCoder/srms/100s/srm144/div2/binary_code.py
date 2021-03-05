class BinaryCode:
    def decode(self, message):
        res = []
        for j in range(2):
            c = [j % 2]
            for i, e in enumerate(message[:-1]):
                n = int(e) - sum(c[i - 1 : i + 2])
                if 0 <= n <= 1:
                    c.append(n)
                else:
                    c = None
                    break
            if c and sum(c[-2:]) != int(message[-1]):
                c = None
            res.append(c)
        return tuple("".join(map(str, e)) if e else "NONE" for e in res)
