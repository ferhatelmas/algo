from sys import maxint

class WinterAndMandarins:
    def getNumber(self, bags, K):
        ls, l, m = sorted(bags), len(bags), maxint
        for i in xrange(l-K+1):
            m = min(m, ls[i+K-1]-ls[i])
        return m
