class HappyCells:
    def getHappy(self, grid):
        lr, lc = len(grid), len(grid[0])

        def orthogonal(i, j):
            res = []
            if j > 0:
                res.append(grid[i][j - 1])
            if j < lc - 1:
                res.append(grid[i][j + 1])
            if i > 0:
                res.append(grid[i - 1][j])
            if i < lr - 1:
                res.append(grid[i + 1][j])
            return "".join(res)

        def diagonal(i, j):
            res = []
            if i > 0 and j > 0:
                res.append(grid[i - 1][j - 1])
            if i < lr - 1 and j < lc - 1:
                res.append(grid[i + 1][j + 1])
            if i > 0 and j < lc - 1:
                res.append(grid[i - 1][j + 1])
            if i < lr - 1 and j > 0:
                res.append(grid[i + 1][j - 1])
            return "".join(res)

        def happy(i, j):
            return orthogonal(i, j), diagonal(i, j)

        c1, c2, c3 = 0, 0, 0
        for i in xrange(lr):
            for j in xrange(lc):
                if grid[i][j] == ".":
                    o, d = happy(i, j)
                    if "." not in o + d:
                        c1 += 1
                    if "." not in o and "." in d:
                        c2 += 1
                    if "." in o and "." not in d:
                        c3 += 1
        return c1, c2, c3
