from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = [max(r) for r in grid]
        cols = [max(c) for c in zip(*grid)]

        s = 0
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                s += min(rows[i], cols[j]) - c
        return s
