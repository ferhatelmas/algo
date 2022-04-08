import itertools


class Solution:
    def permuteUnique(self, nums):
        return list(set(itertools.permutations(nums)))
