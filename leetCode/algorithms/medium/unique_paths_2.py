class Solution:
    def uniquePathsWithObstacles(self, g):
        h = len(g)
        if h == 0:
            return 0
        w = len(g[0])
        if w == 0 or g[0][0] == 1:
            return 0

        g[0][0] = 1
        for i in range(1, w):
            g[0][i] = 0 if g[0][i] == 1 else g[0][i - 1]

        for j in range(1, h):
            g[j][0] = 0 if g[j][0] == 1 else g[j - 1][0]
            for i in range(1, w):
                g[j][i] = 0 if g[j][i] == 1 else g[j - 1][i] + g[j][i - 1]
        return g[h - 1][w - 1]
