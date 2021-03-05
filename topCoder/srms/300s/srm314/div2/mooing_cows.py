from sys import maxint


class MooingCows:
    def dissatisfaction(self, farmland):
        m, l1, l2 = maxint, len(farmland), len(farmland[0])

        def cnt(i, j):
            return sum(
                [
                    (k - i) ** 2 + (l - j) ** 2
                    for k in range(l1)
                    for l in range(l2)
                    if farmland[k][l] == "C"
                ]
            )

        if all([c == "C" for r in farmland for c in r]):
            return cnt(l1 / 2, l2 / 2)
        for i in xrange(l1):
            for j in xrange(l2):
                if farmland[i][j] == "C":
                    m = min(m, cnt(i, j))
        return m
