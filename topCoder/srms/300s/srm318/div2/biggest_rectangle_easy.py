class BiggestRectangleEasy:
    def findArea(self, N):
        m, n = 0, N / 2
        for i in xrange(n + 1):
            m = max(m, i * (n - i))
        return m
