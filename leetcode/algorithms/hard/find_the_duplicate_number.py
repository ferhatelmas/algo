class Solution:
    def findDuplicate(self, nums):
        if len(nums) > 1:
            s, f = nums[0], nums[nums[0]]
            while s != f:
                s, f = nums[s], nums[nums[f]]

            f = 0
            while s != f:
                f, s = nums[f], nums[s]
            return s
        return -1
