class ReversedSum:
    def getReversedSum(self, x, y):
        return int(str(int(str(x)[::-1]) + int(str(y)[::-1]))[::-1])
