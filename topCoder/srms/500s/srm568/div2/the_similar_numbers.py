class TheSimilarNumbers:
    def find(self, lower, upper):
        c = 0
        while lower <= upper:
            c += 1
            lower = 10 * lower + 1
        return c
