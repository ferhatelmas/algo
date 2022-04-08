from itertools import groupby


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        return max(([len(list(g)) for k, g in groupby(nums) if k == 1]) or [0])
