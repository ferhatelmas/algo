from operator import itemgetter


class MaximumScoredNumber:
    def getNumber(self, lowerBound, upperBound):
        def score(n):
            c, s = 0, set()
            for i in xrange(int(n ** 0.5) + 1):
                j = (n - i ** 2) ** 0.5
                if j == int(j) and i not in s:
                    s.add(j)
                    c += 1
            return c

        return sorted(
            [(i, score(i)) for i in xrange(lowerBound, upperBound + 1)],
            key=itemgetter(1, 0),
            reverse=True,
        )[0][0]
