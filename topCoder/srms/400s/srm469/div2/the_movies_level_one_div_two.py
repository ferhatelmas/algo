from itertools import groupby

class TheMoviesLevelOneDivTwo:
    def find(self, n, m, row, seat):
        t = [[0]*m for i in xrange(n)]
        for r, s in zip(row, seat):
            t[r-1][s-1] = 1
        c = 0
        for r in t:
            for k, g in groupby(r):
                if k == 0:
                    n = len(list(g))
                    if n > 1:
                        c += n-1
        return c
