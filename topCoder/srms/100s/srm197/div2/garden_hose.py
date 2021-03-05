class GardenHose:
    def countDead(self, n, rowDist, colDist, hoseDist):
        a, b = n - 2 * (hoseDist / colDist), n - 2 * (hoseDist / rowDist)
        return 0 if min(a, b) <= 0 else a * b
