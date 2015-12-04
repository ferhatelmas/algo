import bisect
import sys


levels = [0, 2, 4, 6]
level_names = ["Done", "Low", "Medium", "High", "Critical"]


def t(a, b):
    n = sum(i != j for i, j in zip(a, b))
    return level_names[bisect.bisect_left(levels, n)]


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        print(t(*(e.strip() for e in test.rstrip().split("|"))))
