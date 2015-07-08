class Solution:
    def majorityElement(self, nums):
        c1 = c2 = a = b = 0
        for e in nums:
            if c1 == 0 or e == a:
                c1 += 1
                a = e
            elif c2 == 0 or e == b:
                c2 += 1
                b = e
            else:
                c1 -= 1
                c2 -= 1
        c1 = c2 = 0
        for e in nums:
            c1 += e == a
            c2 += e == b
        res, l = set(), len(nums)
        if c1 > l / 3:
            res.add(a)
        if c2 > l / 3:
            res.add(b)
        return list(res)
