from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s, d = 0, 0
        for x in nums:
            if x < 10:
                s += x
            else:
                d += x
        return s != d
