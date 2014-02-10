class RoadOrFlightEasy:
    def minTime(self, N, roadTime, flightTime, K):
        c, res = 0, 0
        for r, f in sorted(zip(roadTime, flightTime), key=lambda (r, f): f-r):
            if f < r and c < K:
                res += f
                c += 1
            else:
                res += r
        return res
