class TrappingRabbit:
    def findMinimumTime(self, trapX, trapY):
        return min(x+y-2 for x, y in zip(trapX, trapY))
