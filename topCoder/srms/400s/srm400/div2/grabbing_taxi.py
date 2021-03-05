class GrabbingTaxi:
    def minTime(self, tXs, tYs, gX, gY, walkTime, taxiTime):
        def time(x1, y1, x2, y2, walk=False):
            dist = abs(x1 - x2) + abs(y1 - y2)
            if walk:
                return dist * walkTime
            return dist * taxiTime

        w = time(0, 0, gX, gY, walk=True)
        ls = [
            time(0, 0, x, y, walk=True) + time(x, y, gX, gY) for x, y in zip(tXs, tYs)
        ]
        return min([w] + ls)
