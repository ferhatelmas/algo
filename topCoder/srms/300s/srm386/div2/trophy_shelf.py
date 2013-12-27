class TrophyShelf:
    def countVisible(self, trophies):
        m, l = trophies[0], 1
        for e in trophies[1:]:
            if e > m:
                l += 1
                m = e
        m, r = trophies[-1], 1
        for e in trophies[::-1][1:]:
            if e > m:
                r += 1
                m = e
        return l, r
