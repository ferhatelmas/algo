class LittleElephantAndDouble:
    def getAnswer(self, A):
        ls = sorted(A)
        for i, j in zip(ls, ls[1:]):
            while i < j:
                i *= 2
            if i != j:
                return 'NO'
        return 'YES'
