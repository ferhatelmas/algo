from functools import reduce
from itertools import combinations
from operator import xor
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums) + 1):
            for c in combinations(nums, i):
                s += reduce(xor, c, 0)
        return s
