from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        a, b = points[0]
        s = 0
        for x, y in points[1:]:
            s += max(abs(x - a), abs(y - b))
            a, b = x, y
        return s
