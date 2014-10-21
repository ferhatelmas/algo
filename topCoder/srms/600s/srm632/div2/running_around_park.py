class RunningAroundPark:
    def numberOfLap(self, N, d):
        x, c = d[0], 1
        for e in d[1:]:
            if e <= x:
                c += 1
            x = e
        return c
