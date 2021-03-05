from math import pi


class RecursiveFigures:
    def getArea(self, sideLength, K):
        return sum(
            (sideLength ** 2) * (pi - 2) / (4 * 2 ** i) for i in xrange(0, K - 1)
        ) + (pi * sideLength ** 2 / 2 ** (K + 1))
