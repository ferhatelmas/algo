from itertools import groupby

class TaroGrid:
    def getNumber(self, grid):
        return max(len(list(g))
                   for e in zip(*grid)
                   for k, g in groupby(e))
