class TheBrickTowerEasyDivTwo:
    def find(self, redCount, redHeight, blueCount, blueHeight):
        h = redHeight + blueHeight

        def c(i, j):
            r = min(i, j) * h
            if i == j:
                return r
            return r + (redHeight if i > j else blueHeight)

        t = set()
        for i in xrange(redCount + 1):
            for j in xrange(blueCount + 1):
                if i or j:
                    t.add(c(i, j))
        return len(t)
