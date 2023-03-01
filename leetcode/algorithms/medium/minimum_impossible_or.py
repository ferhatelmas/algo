from typing import List


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = set(nums)
        n = 1
        while n in s:
            n *= 2
        return n
