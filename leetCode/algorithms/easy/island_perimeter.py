from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 0:
                    continue
                if i == 0 or grid[i - 1][j] == 0:
                    cnt += 1
                if j == 0 or row[j - 1] == 0:
                    cnt += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    cnt += 1
                if j == len(row) - 1 or row[j + 1] == 0:
                    cnt += 1
        return cnt
