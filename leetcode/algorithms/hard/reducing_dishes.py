from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ss, l, m = sorted(satisfaction), len(satisfaction), 0
        for i in range(0, l):
            m = max(m, sum(t * s for t, s in enumerate(ss[i:], start=1)))
        return m
