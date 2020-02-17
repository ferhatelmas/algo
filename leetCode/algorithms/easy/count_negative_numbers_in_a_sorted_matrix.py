from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(e < 0 for r in grid for e in r)
