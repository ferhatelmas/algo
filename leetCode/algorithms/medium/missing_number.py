class Solution(object):
        def missingNumber(self, nums):
            n = len(nums)
            return (n * (n+1)) / 2 - sum(nums)
