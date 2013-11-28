import math

class WidgetRepairs:
    def days(self, arrivals, numPerDay):
        s, c = 0, 0
        for a in arrivals:
            s += a
            if s > 0:
                c += 1
            s = 0 if s < numPerDay else s-numPerDay
        c += int(math.ceil(float(s) / numPerDay))
        return c
