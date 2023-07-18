from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        l = len(nums)
        return sum(e**2 for i, e in enumerate(nums, start=1) if l % i == 0)
