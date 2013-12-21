class SkewSymmetric:
    def minChanges(self, M):
        c, l = 0, len(M)
        M = map(lambda s: map(int, s.split()), M)
        for i in xrange(l):
            for j in xrange(i):
                if M[i][j] != -M[j][i]:
                    c += 1
            if M[i][i] != 0:
                c += 1
        return c
