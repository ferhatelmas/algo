class PalindromizationDiv2:
    def getMinimumCost(self, X):
        def p(n):
            s = str(n)
            return s == s[::-1]
        return next(i for i in xrange(X+1) if p(X+i) or p(X-i))
