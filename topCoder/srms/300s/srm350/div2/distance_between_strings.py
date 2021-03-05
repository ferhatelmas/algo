class DistanceBetweenStrings:
    def getDistance(self, a, b, letterSet):
        a, b, c = map(lambda s: s.lower(), [a, b, letterSet])
        return sum(map(lambda e: (a.count(e) - b.count(e)) ** 2, c))
