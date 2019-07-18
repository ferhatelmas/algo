from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = {}
        for i, e in enumerate(nums):
            if e in counts:
                a, b, c = counts[e]
                counts[e] = [a, i, c+1]
            else:
                counts[e] = [i, i, 1]

        d, m = 0, len(nums)
        for a, b, c in counts.values():
            if c > d:
                m = b - a + 1
            elif c == d:
                m = min(m, b - a + 1)
            d = max(d, c)
        return m
