from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s = 1
        for n in nums:
            if n < 0:
                s *= -1
            elif n == 0:
                return 0
        return -1 if s < 0 else 1
