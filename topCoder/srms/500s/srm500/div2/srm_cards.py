class SRMCards:
    def maxTurns(self, cards):
        c, s, k = sorted(cards), 0, 1
        for i, j in zip(c, c[1:]):
            if j-i < 2:
                k += 1
            else:
                s += (k+1) / 2
                k = 1
        s += (k+1) / 2
        return s
