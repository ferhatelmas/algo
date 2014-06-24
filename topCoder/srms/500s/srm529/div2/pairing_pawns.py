class PairingPawns:
    def savedPawnCount(self, start):
        s = list(start)
        for i in xrange(len(start)-1, 0, -1):
            s[i-1] += s[i] / 2
        return s[0]
