class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[1 - int(matrix[i][j] == "0") for j in xrange(n)] for i in xrange(m)]

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0

        return max([max(i) for i in dp]) ** 2
