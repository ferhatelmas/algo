from itertools import groupby

class FourBlocksEasy:
    def maxScore(self, grid):
        s = 0
        for k, g in groupby(zip(*grid)):
            t = len(list(g))
            if k == ('.', '.'):
                s += (t/2) * 16 + t%2 * 2
            else:
                s += 2 * t
        return s
