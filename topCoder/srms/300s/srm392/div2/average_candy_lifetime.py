class AverageCandyLifetime:
    def getAverage(self, eatenCandies):
        d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        s = 0.0
        for i, e in enumerate(eatenCandies):
            s += sum(d[: i + 1]) * e
        return s / sum(eatenCandies)
