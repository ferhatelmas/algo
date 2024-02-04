from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        d, c = 0, 0
        for n in nums:
            d += n
            if d == 0:
                c += 1
        return c
