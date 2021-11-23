from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        m = 0
        for i, a in enumerate(colors):
            for j, b in enumerate(colors):
                if j > i and a != b:
                    m = max(m, j - i)
        return m
