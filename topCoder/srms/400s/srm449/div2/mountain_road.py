class MountainRoad:
    def findDistance(self, start, finish):
        return 2 ** 0.5 * (max(finish) - min(start))
