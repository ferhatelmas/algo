class MagicalGirlLevelOneDivTwo:
    def theMinDistance(self, d, x, y):
        return min(
            sorted(
                (a ** 2 + b ** 2) ** 0.5
                for a in xrange(x - d, x + d + 1)
                for b in xrange(y - d, y + d + 1)
            )
        )
