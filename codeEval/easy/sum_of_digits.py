import sys

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print sum(map(int, test.strip()))
test_cases.close()
