from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        for i in range(1, n):
            dp[i] = min(dp[i - 1], cost[i])
        return dp
