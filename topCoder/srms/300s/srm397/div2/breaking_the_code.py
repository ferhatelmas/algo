class BreakingTheCode:
    def decodingEncoding(self, code, message):
        if "a" <= message[0] <= "z":
            return "".join("{0:02}".format(code.index(e) + 1) for e in message)
        d = dict(("{0:02}".format(i), e) for i, e in enumerate(code, 1))
        return "".join(d[message[i : i + 2]] for i in xrange(0, len(message), 2))
