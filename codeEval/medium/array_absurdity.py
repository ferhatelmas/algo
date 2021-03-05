import sys


def duplicate(n, s):
    return s - (n ** 2 - 3 * n + 2) / 2


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    if test.strip() != "":
        n, l = test.split(";")
        print duplicate(int(n), sum(map(int, l.split(","))))
test_cases.close()
