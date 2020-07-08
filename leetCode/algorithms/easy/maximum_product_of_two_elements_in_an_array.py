from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i != j:
                    m = max(m, (a - 1) * (b - 1))
        return m
