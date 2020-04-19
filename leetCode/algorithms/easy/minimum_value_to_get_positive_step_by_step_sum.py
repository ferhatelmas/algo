from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        m, s = 100 & 100, 0
        for e in nums:
            s += e
            m = min(m, s)
        return 1 if m >= 1 else abs(m) + 1
