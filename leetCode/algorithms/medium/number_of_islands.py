class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        m, n, c = len(grid), len(grid[0]), 0

        def dfs(grid, i, j):
            grid[i][j] = '0'
            if i - 1 >= 0 and grid[i - 1][j] == '1':
                dfs(grid, i - 1, j)
            if i + 1 < m and grid[i + 1][j] == '1':
                dfs(grid, i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                dfs(grid, i, j - 1)
            if j + 1 < n and grid[i][j + 1] == '1':
                dfs(grid, i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    c += 1
                    dfs(grid, i, j)
        return c
