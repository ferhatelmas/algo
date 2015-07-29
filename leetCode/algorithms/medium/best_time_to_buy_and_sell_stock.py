class Solution:
    def maxProfit(self, prices):
        res = m = 0
        for i, j in zip(prices, prices[1:]):
            res += j - i
            res = max(0, res)
            m = max(res, m)
        return m
