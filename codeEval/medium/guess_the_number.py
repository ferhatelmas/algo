import sys


def guess(n, ls):
    low, high = 0, n
    for g in ls:
        m = int(round((low + high) / 2.0))
        if g == "Lower":
            high = m - 1
        elif g == "Higher":
            low = m + 1
        else:
            return m


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        parts = test.rstrip().split()
        print guess(int(parts[0]), parts[1:])
