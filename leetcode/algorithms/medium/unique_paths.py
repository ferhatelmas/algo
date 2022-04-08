class Solution:
    def uniquePaths(self, m, n):
        r = [[0] * n for _ in xrange(m)]
        r[0][0] = 1
        for i in xrange(m):
            for j in xrange(n):
                if i:
                    r[i][j] += r[i - 1][j]
                if j:
                    r[i][j] += r[i][j - 1]
        return r[m - 1][n - 1]
