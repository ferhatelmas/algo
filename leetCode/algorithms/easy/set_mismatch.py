class Solution(object):
    def findErrorNums(self, nums):
        prev = dup = s = 0
        for i in sorted(nums):
            if not dup and i == prev:
                dup = i
            s, prev = s + i, i
        l = len(nums)
        return (dup, (l * (l + 1) / 2) + dup - s)
