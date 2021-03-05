import sys
from operator import itemgetter


def get_distance(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5


def find_closest_pair(ls):
    ls = sorted(ls, key=itemgetter(0, 1))
    dist, m = [], 40000
    for i in range(len(ls) - 1):
        m = min(m, get_distance(ls[i], ls[i + 1]))
    if m > 10000:
        return "INFINITY"
    else:
        return "%.4f" % m


points, n = [], 0
test_cases = open(sys.argv[1], "r")
for test in test_cases:
    if n == 0:
        if len(points) > 0:
            print find_closest_pair(points)
            points = []
        n = int(test.strip())
        if n == 0:
            break
    else:
        points.append(map(int, test.split()))
        n -= 1
test_cases.close()
