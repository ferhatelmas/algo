class Solution:
    def findMin(self, nums):
        l, h, m = 0, len(nums)-1, 0

        while l < h:
            m = l + (h - l) / 2

            if nums[m] > nums[h]:
                l = m + 1
            elif nums[m] < nums[h]:
                h = m
            else:
                h -= 1
        return nums[l]
