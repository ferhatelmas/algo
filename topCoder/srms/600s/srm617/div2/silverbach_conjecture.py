class SilverbachConjecture:
    def solve(self, n):
        ls = [True] * 2001
        for i in xrange(2, 2001):
            if ls[i]:
                for j in xrange(2*i, 2001, i):
                    ls[j] = False
        for i in xrange(2, n-1):
            if not ls[i] and not ls[n-i]:
                return (i, n-i)
