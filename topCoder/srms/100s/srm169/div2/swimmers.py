class Swimmers:
    def getSwimTimes(self, distances, speeds, current):
        def time(d, s):
            if d == 0:
                return 0
            if s <= current:
                return -1
            d = float(d)
            return int(d/(s+current) + d/(s-current))
        return map(time, distances, speeds)
