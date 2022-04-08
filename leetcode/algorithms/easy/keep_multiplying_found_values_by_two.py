from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        o = original
        while o in s:
            o *= 2
        return o
