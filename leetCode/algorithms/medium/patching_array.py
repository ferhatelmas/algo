class Solution:
    def minPatches(self, nums, n):
        if n == 0:
            return 0
        res = m = 0
        for e in nums:
            while e > m + 1:
                m, res = 2*m + 1, res + 1
                if m >= n:
                    return res
            m += e
            if m >= n:
                return res
        while m < n:
            m, res = 2*m + 1, res + 1
        return res
