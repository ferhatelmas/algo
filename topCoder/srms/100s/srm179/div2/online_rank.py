class OnLineRank:
    def calcRanks(self, k, scores):
        def rank(l, n):
            return 1 + sorted(l, reverse=True).index(n)

        return sum(
            map(
                lambda (i, n): rank(scores[max(i - k, 0) : i + 1], n), enumerate(scores)
            )
        )
