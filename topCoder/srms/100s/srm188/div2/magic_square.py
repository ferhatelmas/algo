class MagicSquare:
    def missing(self, square):
        sums = map(lambda i: sum(square[i : i + 3]), range(0, 9, 3))
        return max(sums) - min(sums) - 1
