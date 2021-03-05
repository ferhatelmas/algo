from sys import maxint


class FoxAndSightseeing:
    def getMin(self, position):
        l, m = len(position), maxint
        for i in xrange(1, l - 1):
            s = 0
            for j in xrange(1, l):
                if i == j:
                    continue
                p = j - 2 if j == i + 1 else j - 1
                s += abs(position[j] - position[p])
            m = min(m, s)
        return m
