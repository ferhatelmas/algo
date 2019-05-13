class Solution(object):
    def maxCoins(self, nums):
        n, ns = len(nums), [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for ln in range(1, n + 1):
            for l in range(1, n - ln + 2):
                r = l + ln - 1
                for i in range(l, r + 1):
                    dp[l][r] = max(dp[l][r], ns[l - 1] * ns[i] * ns[r + 1] +
                                   dp[l][i - 1] + dp[i + 1][r])
        return dp[1][n]
