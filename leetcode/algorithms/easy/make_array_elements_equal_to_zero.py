from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s, p, r = sum(nums), 0, 0
        for e in nums:
            if e > 0:
                p += e
                s -= e
            else:
                if p == s:
                    r += 2
                elif abs(p - s) == 1:
                    r += 1
        return r
