from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        d, area = 0, 0
        for a, b in dimensions:
            n = a**2 + b**2
            if n > d:
                d = n
                area = a * b
            elif n == d:
                area = max(area, a * b)
        return area
