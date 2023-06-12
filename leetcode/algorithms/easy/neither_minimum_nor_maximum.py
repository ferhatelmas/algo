from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        for e in nums:
            if e != a and e != b:
                return e
        return -1
