class PirateTreasure:
    def getDistance(self, steps, directions):
        i, j, k = 0, 0, 2**.5
        for s, d in zip(steps, directions):
            if d == 'NORTH':
                j += s
            elif d == 'NORTHEAST':
                i += s / k
                j += s / k
            elif d == 'EAST':
                i += s
            elif d == 'SOUTHEAST':
                i += s / k
                j -= s / k
            elif d == 'SOUTH':
                j -= s
            elif d == 'SOUTHWEST':
                i -= s / k
                j -= s / k
            elif d == 'WEST':
                i -= s
            else:
                i -= s / k
                j += s / k
        return (i**2 + j **2)**0.5
