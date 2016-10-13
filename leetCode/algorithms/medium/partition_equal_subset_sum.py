class Solution(object):
    def canPartition(self, nums):
        l, s = len(nums) + 1, sum(nums)
        if s % 2:
            return False
        p = [[True] * l] + [[False] * l for _ in range(s/2)]
        for i in range(1, s/2 + 1):
            for j in range(1, l):
                p[i][j] = p[i][j-1] or i >= nums[j-1] and p[i-nums[j-1]][j-1]
        return p[s/2][l-1]
