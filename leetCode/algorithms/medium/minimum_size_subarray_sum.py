class Solution:
    def minSubArrayLen(self, s, nums):
        ll = len(nums)
        n = l = 0
        r = ll + 1
        for i, e in enumerate(nums):
            n += e
            while n >= s:
                r = min(r, i - l + 1)
                n -= nums[l]
                l += 1
        return (0, r)[r <= ll]
