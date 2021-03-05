class InequalityChecker:
    def getDifferences(self, n):
        s, r = 2 * (sum(map(lambda i: 2 * i ** 3, xrange(n))) + n ** 3) - n ** 4, 4
        while s % 2 == 0 and r % 2 == 0:
            s /= 2
            r /= 2
        return s, r
