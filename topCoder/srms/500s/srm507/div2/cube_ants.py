class CubeAnts:
    def getMinimumSteps(self, pos):
        diff = {0:0, 1:1, 2:2, 3:1, 4:1, 5:2, 6:3, 7:2}
        return max(diff[i] for i in set(pos))
