class BunnyExamAfter:
    def getMaximum(self, black, gray, white):
        c = 0
        for b, g, w in zip(black, gray, white):
            if b != g and b != w:
                if g == w:
                    c += 2
                else:
                    c += 1
            elif g != w:
                c += 1
        return c
