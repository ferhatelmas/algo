from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        m, s = 0, []
        for e in nums:
            if e > m:
                m = e
            s.append(e + m + (s[-1] if s else 0))
        return s
