class RoyalTreasurer:
    def minimalArrangement(self, A, B):
        return sum(map(lambda (a, b): a * b, zip(sorted(A), sorted(B, reverse=True))))
