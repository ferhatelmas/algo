class RectangleCoveringEasy:
    def solve(self, holeH, holeW, boardH, boardW):
        minh, maxh = min(holeH, holeW), max(holeH, holeW)
        minb, maxb = min(boardH, boardW), max(boardH, boardW)
        if (minh < minb and maxh <= maxb) or (minh <= minb and maxh < maxb):
            return 1
        return -1
