from bisect import bisect


class UnluckyNumbers:
    def getCount(self, luckySet, n):
        if n in luckySet:
            return 0
        ls = sorted(luckySet)
        k = bisect(ls, n)
        i, j = 1 if k == 0 else ls[k - 1] + 1, ls[k] - 1
        return (n - i + 1) * (j - n + 1) - 1
