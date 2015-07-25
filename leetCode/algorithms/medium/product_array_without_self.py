class Solution:
    def productExceptSelf(self, nums):
        lg, l, r = len(nums), 1, 1
        res = [1] * lg
        for i, e in enumerate(nums):
            res[i] *= l
            res[lg-1-i] *= r
            l *= e
            r *= nums[lg-1-i]
        return res
