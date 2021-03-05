import sys


class Car:
    def __init__(self, i, m, a, b):
        self.i = int(i)
        self.m = m / 3600
        self.a = a
        self.b = b

    def calculate_lap_time(self, t, total_track):
        total, path = self.a, (self.m * self.a) / 2.0
        for d in t:
            n = (self.m * (180 - d)) / 180.0
            t1 = ((self.m - n) * self.b) / self.m
            total += t1
            l1 = ((self.m + n) * t1) / 2.0
            path += l1

            t2 = ((self.m - n) * self.a) / self.m
            total += t2
            l2 = ((self.m + n) * t2) / 2.0
            path += l2
        total += (total_track - path) / self.m
        self.lap_time = total

    def __cmp__(self, o):
        return cmp(self.lap_time, o.lap_time)

    def __str__(self):
        return "{} {:.2f}".format(self.i, self.lap_time)


cars = []
test_cases = open(sys.argv[1], "r")
for i, test in enumerate(test_cases):
    if i:
        cars.append(Car(*map(float, test.split())))
    else:
        track = map(float, test.split())
        total = sum(track[::2])
        track = track[1::2]
test_cases.close()

map(lambda c: c.calculate_lap_time(track, total), cars)
print "\n".join(map(str, sorted(cars)))
