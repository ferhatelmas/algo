from itertools import groupby

class ColorfulTilesEasy:
    def theMin(self, room):
        return sum(len(list(g))//2 for _, g in groupby(room))
