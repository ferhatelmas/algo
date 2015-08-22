class Solution:
    def r(self, nums):
        a = b = res = 0
        for e in nums:
            res = max(b + e, a)
            b, a = a, res
        return res

    def rob(self, nums):
        if len(nums) < 2:
            return sum(nums)
        return max(self.r(nums[1:]), self.r(nums[:-1]))
