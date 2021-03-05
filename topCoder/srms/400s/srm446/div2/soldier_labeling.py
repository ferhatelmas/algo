class SoldierLabeling:
    def count(self, n, lowerBound, upperBound):
        return max(0, min(10 ** upperBound - 1, n) - 10 ** (lowerBound - 1) + 1)
