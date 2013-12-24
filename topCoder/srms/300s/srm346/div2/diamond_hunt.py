class DiamondHunt:
    def countDiamonds(self, mine):
        c, l, f = 0, len(mine), True
        while f:
            f = False
            for i in xrange(l-1):
                if mine[i:i+2] == '<>':
                    mine, l = mine[:i] + mine[i+2:], l-2
                    c += 1
                    f = True
                    break
        return c
