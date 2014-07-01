class TypoCoderDiv2:
    def count(self, rating):
        b, c = False, 0
        for r in rating:
            if r >= 1200 and not b:
                c += 1
                b = True
            elif r < 1200 and b:
                c += 1
                b = False
        return c
