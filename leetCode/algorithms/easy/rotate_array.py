class Solution:

    def rotate(self, nums, k):
        l = len(nums)
        k %= l
        if k < l:
            c, i, p = 0, 0, nums[0]
            for j in xrange(l):
                i = (i + k) % l
                p, nums[i] = nums[i], p
                c += k
                if c % l == 0:
                    c, i = 0, (i + 1) % l
                    p = nums[i]
