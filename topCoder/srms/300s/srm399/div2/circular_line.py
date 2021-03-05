class CircularLine:
    def longestTravel(self, t):
        m, l = 0, len(t)
        for i in xrange(l):
            for j in xrange(i + 1, l):
                m = max(m, min(sum(t[i:j]), sum(t[:i]) + sum(t[j:])))
        return m
