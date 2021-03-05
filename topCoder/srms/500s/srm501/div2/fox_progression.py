class FoxProgression:
    def theCount(self, seq):
        if len(seq) == 1:
            return -1
        a, m = seq[1] - seq[0], seq[1] / float(seq[0])
        af, mf = True, m == int(m)
        c = sum((af, mf))
        for i, j in zip(seq[1:], seq[2:]):
            if af and j - i != a:
                af = False
                c -= 1
            if mf and j / float(i) != m:
                mf = False
                c -= 1
            if not af and not mf:
                break
        if af and mf and seq[-1] + a == seq[-1] * m:
            c -= 1
        return c
