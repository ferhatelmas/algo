class SnowyWinter:
    def snowyHighwayLength(self, startPoints, endPoints):
        road = [False] * 10001
        for s, e in zip(startPoints, endPoints):
            for i in xrange(s, e):
                road[i] = True
        return len([e for e in road if e])
