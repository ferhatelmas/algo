class DiagonalDisproportion:
    def getDisproportion(self, matrix):
        r = 0
        for i, s in enumerate(matrix):
            r += int(s[i]) - int(s[-i - 1])
        return r
