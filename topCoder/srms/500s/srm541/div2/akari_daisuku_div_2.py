class AkariDaisukiDiv2:
    def countTuples(self, S):
        l, c = len(S), 0
        for i in xrange(1, l):
            for j in xrange(i+1, l):
                for k in xrange(j+1, l):
                    for m in xrange(k+1, l):
                        c += S[i:j] == S[k:m]
        return c
