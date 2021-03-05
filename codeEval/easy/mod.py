import sys

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    n, m = map(int, test.split(","))
    print n - m * (n // m)
test_cases.close()
