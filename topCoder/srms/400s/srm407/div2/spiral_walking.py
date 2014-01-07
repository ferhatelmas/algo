class SpiralWalking:
    def totalPoints(self, levelMap):
        lr, lc = len(levelMap), len(levelMap[0])
        v = [[True]*lc for _ in xrange(lr)]
        c, h, f, i, j, x, t = 0, True, True, 0, 0, 0, lr*lc
        while True:
            x += 1
            if x == t:
                c += int(levelMap[i][j])
                break
            if h and f:
                if j < lc-1 and v[i][j+1]:
                    c += int(levelMap[i][j])
                    v[i][j] = False
                    j += 1
                else:
                    h = not h
                    i += 1
            elif h and not f:
                if j > 0 and v[i][j-1]:
                    c += int(levelMap[i][j])
                    v[i][j] = False
                    j -= 1
                else:
                    h = not h
                    i -= 1
            elif not h and f:
                if i < lr-1 and v[i+1][j]:
                    c += int(levelMap[i][j])
                    v[i][j] = False
                    i += 1
                else:
                    j -= 1
                    h = not h
                    f = not f
            else:
                if i > 0 and v[i-1][j]:
                    c += int(levelMap[i][j])
                    v[i][j] = False
                    i -= 1
                else:
                    j += 1
                    h = not h
                    f = not f
        return c
