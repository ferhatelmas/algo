class RainyRoad:
    def isReachable(self, road):
        for i, j in zip(*road):
            if i == j == "W":
                return "NO"
        return "YES"
