import sys


def arm(n):
    l = len(n)
    return sum(map(lambda e: int(e) ** l, n)) == int(n)


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print arm(test.strip())
test_cases.close()
