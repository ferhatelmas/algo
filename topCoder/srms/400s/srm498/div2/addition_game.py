class AdditionGame:
    def getMaximumPoints(self, A, B, C, N):
        l = [A, B, C]

        def choose(l):
            m = max(l)
            if m < 1:
                return 0
            l[l.index(m)] -= 1
            return m

        return sum(choose(l) for i in xrange(N))
