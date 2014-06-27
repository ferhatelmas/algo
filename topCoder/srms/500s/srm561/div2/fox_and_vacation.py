class FoxAndVacation:
    def maxCities(self, total, d):
        d, i, l = sorted(d), 0, len(d)
        while i < l and total >= d[i]:
            total -= d[i]
            i += 1
        return i
