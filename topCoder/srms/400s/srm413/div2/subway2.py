class Subway2:
    def minTime(self, length, maxAcceleration, maxVelocity):
        t1 = (length / float(maxAcceleration)) ** 0.5
        if maxAcceleration * t1 <= maxVelocity:
            return 2 * t1
        t2 = maxVelocity / float(maxAcceleration)
        return (length - maxAcceleration * t2 * t2) / maxVelocity + 2 * t2
