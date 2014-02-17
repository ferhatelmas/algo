class LinearTravellingSalesman:
    def findMinimumDistance(self, x, y):
        ls = sorted(zip(x, y))
        return sum(abs(y2-y1) + abs(x2-x1) for (x1, y1), (x2, y2) in zip(ls, ls[1:]))
