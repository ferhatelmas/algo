class EasyHomework:
    def determineSign(self, A):
        c = True
        for e in A:
            if e < 0:
                c = not c
            elif e == 0:
                return 'ZERO'
        return 'POSITIVE' if c else 'NEGATIVE'
