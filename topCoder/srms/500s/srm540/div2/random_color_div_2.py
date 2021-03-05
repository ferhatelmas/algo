class RandomColoringDiv2:
    def getCount(self, maxR, maxG, maxB, startR, startG, startB, d1, d2):
        c = 0
        for r in xrange(maxR):
            for g in xrange(maxG):
                for b in xrange(maxB):
                    c += (
                        d1
                        <= max(abs(r - startR), abs(g - startG), abs(b - startB))
                        <= d2
                    )
        return c
