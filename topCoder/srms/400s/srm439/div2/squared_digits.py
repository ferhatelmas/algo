class SquareOfDigits:
    def getMax(self, data):
        lx, ly = len(data), len(data[0])
        for s in xrange(min(lx, ly), 1, -1):
            for i in xrange(lx-s+1):
                for j in xrange(ly-s+1):
                    if data[i][j] == data[i+s-1][j] == data[i][j+s-1] == data[i+s-1][j+s-1]:
                        return s*s
        return 1
