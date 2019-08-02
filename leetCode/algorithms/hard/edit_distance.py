class Solution:
    def minDistance(self, w1, w2):
        m, n = len(w1), len(w2)
        c = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            c[i][0] = i
        for i in range(n + 1):
            c[0][i] = i
        for i, a in enumerate(w1):
            for j, b in enumerate(w2):
                if a == b:
                    c[i + 1][j + 1] = c[i][j]
                else:
                    c[i + 1][j + 1] = 1 + min(c[i][j], c[i + 1][j], c[i][j + 1])
        return c[m][n]
