from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        p = None
        for i, e in enumerate(nums):
            n = e % 2
            if i > 0 and p == n:
                return False
            p = n
        return True
