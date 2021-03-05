from itertools import groupby


class ManySquares:
    def howManySquares(self, sticks):
        return sum(len(list(g)) / 4 for k, g in groupby(sorted(sticks)))
