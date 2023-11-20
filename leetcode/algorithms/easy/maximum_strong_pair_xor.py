from typing import List
from itertools import combinations


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        m = 0
        for x, y in combinations(nums, 2):
            if abs(x - y) <= min(x, y):
                if x ^ y >= m:
                    m = x ^ y
        return m
