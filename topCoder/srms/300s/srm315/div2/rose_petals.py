class RosePetals:
    def getScore(self, dice):
        n = [0, 0, 0, 2, 0, 4, 0]
        return sum(map(lambda i: n[i], dice))
