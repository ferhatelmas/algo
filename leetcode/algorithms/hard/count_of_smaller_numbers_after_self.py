class Solution:
    def countSmaller(self, nums):
        l = len(nums)
        res, index = [0] * l, range(l - 1, -1, -1)
        if l > 0:
            m = abs(min(nums))
            nums = [e + m for e in nums]

        def f(ind, m):
            if m == 0 or len(ind) < 2:
                return

            low, high, ls = [], [], 0
            for i, e in enumerate(ind):
                if (nums[e] & m) == m:
                    res[e] += ls
                    high.append(e)
                else:
                    ls += 1
                    low.append(e)
            f(low, m >> 1)
            f(high, m >> 1)

        f(index, 1 << 31)
        return res
