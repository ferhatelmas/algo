from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a, s = 0, set()
        for r in grid:
            for c in r:
                if c in s:
                    a = c
                s.add(c)
        for i in range(1, len(grid) ** 2 + 1):
            if i not in s:
                return [a, i]
