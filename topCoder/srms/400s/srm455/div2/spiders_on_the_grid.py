class SpidersOnTheGrid:
    def find(self, A):
        lr, lc = len(A), len(A[0])
        s = [[0] * lc for _ in xrange(lr)]
        for i, r in enumerate(A):
            for j, c in enumerate(r):
                if c == 'N':
                    if i > 0:
                        s[i-1][j] += 1
                elif c == 'S':
                    if i < lr-1:
                        s[i+1][j] += 1
                elif c == 'E':
                    if j < lc-1:
                        s[i][j+1] += 1
                else:
                    if j > 0:
                        s[i][j-1] += 1
        return sum(c == 0 for r in s for c in r)
