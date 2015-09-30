class Solution:
    def searchRange(self, nums, target):
        s, e = 0, len(nums)
        while s < e:
            m = (s + e) // 2
            if nums[m] >= target:
                e = m
            else:
                s = m + 1
        l, s, e = s, 0, len(nums)
        while s < e:
            m = (s + e) // 2
            if nums[m] > target:
                e = m
            else:
                s = m + 1
        return [-1, -1] if l == s else [l, s-1]
