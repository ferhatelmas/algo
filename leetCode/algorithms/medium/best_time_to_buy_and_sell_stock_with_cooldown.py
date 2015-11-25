class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        sell, buy, psell, pbuy = 0, -prices[0], 0, 0
        for p in prices:
            buy, pbuy = max(psell - p, buy), buy
            sell, psell = max(pbuy + p, sell), sell
        return sell
