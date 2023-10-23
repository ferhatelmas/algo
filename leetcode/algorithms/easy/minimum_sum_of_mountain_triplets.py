from itertools import combinations
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        ls = [i + j + k for i, j, k in combinations(nums, 3) if i < j and k < j]
        return -1 if not ls else min(ls)
