class ComparerInator:
    def makeProgram(self, A, B, wanted):
        i, j, m, n = (True,) * 4
        for a, b, w in zip(A, B, wanted):
            i = i and a == w
            j = j and b == w
            m = m and min(a, b) == w
            n = n and max(a, b) == w
        if i or j:
            return 1
        elif m or n:
            return 7
        else:
            return -1
