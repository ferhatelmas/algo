import sys


class Solution:
    def minPathSum(self, grid):
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if i == 0 and j == 0:
                    continue
                up = sys.maxint if i == 0 else grid[i-1][j]
                left = sys.maxint if j == 0 else grid[i][j-1]
                grid[i][j] += min(up, left)
        return grid[-1][-1]
