from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s = 0
        for i, e in enumerate(nums):
            if k == sum(j == "1" for j in bin(i)[2:]):
                s += e
        return s
