class MagicStonesStore:
    def ableToDivide(self, n):
        s = [True] * (2*n+1)
        for i in xrange(2, 2*n+1):
            if s[i]:
                for j in xrange(2*i, 2*n+1, i):
                    s[j] = False
        for i in xrange(2, n+1):
            if s[i] and s[2*n-i]:
                return 'YES'
        return 'NO'
