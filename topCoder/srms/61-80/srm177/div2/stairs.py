class Stairs:
    def designs(self, maxHeight, minWidth, totalHeight, totalWidth):
        c = 0
        for r in xrange(1, maxHeight+1):
            if totalHeight%r == 0:
                n = totalHeight / r
                if n > 1 and totalWidth%(n-1) == 0 and totalWidth / (n-1) >= minWidth:
                    c += 1
        return c
