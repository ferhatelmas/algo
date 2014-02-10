class TrappingRabbit:
    def findMinimumTime(self, trapX, trapY):
        return sorted(x+y-2 for x, y in zip(trapX, trapY))[0]
