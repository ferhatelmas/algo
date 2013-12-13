class GridGenerator:
    def generate(self, row, col):
        l = len(row)
        r = [list(row)] + [[col[i]] + [0]*(l-1) for i in xrange(1, l)]
        for i in xrange(1, l):
            for j in xrange(1, l):
                r[i][j] = r[i][j-1] + r[i-1][j-1] + r[i-1][j]
        return r[l-1][l-1]
