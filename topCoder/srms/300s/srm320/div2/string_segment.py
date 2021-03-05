from itertools import groupby


class StringSegment:
    def average(self, s):
        a, b = 0, 0
        for k, g in groupby(s):
            a += len(list(g))
            b += 1
        return float(a) / b
