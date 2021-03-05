class FowlRoad:
    def crossings(self, roadY, bobX, bobY):
        c, f = 0, 0
        for e in map(lambda e: e - roadY, bobY):
            if e < 0 and f > 0 or (e > 0 and f < 0):
                c += 1
                f = e
            elif e != 0 and f == 0:
                f = e
        return c
