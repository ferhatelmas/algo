class MinimalDifference:
    def findNumber(self, A, B, C):
        def ss(n):
            return sum(int(a) for a in str(n))

        c = ss(C)

        def diff(i):
            return abs(ss(i) - c)

        return sorted(xrange(A, B + 1), key=diff)[0]
