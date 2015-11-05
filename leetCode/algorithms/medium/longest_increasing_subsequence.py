import bisect


class Solution:
    def lengthOfLIS(self, nums):
        dp = []
        for n in nums:
            if not dp or dp[-1] < n:
                dp.append(n)
            else:
                i = bisect.bisect_left(dp, n)
                if i < 0:
                    dp.append(n)
                else:
                    dp[i] = n
        return len(dp)
