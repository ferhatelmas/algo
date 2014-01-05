class DreamingAboutCarrots:
    def carrotsBetweenCarrots(self, x1, y1, x2, y2):
        (x1, x2), (y1, y2) = sorted([x1, x2]), sorted([y1, y2])
        dx, dy = x2-x1, y2-y1
        return sum(
            (x-x1)*dy - (y-y1)*dx == 0
            for x in xrange(x1, x2+1)
            for y in xrange(y1, y2+1)
        ) - 2
