import sys

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    s, tr = test.strip().split(",")
    print s[::-1].count(tr[::-1], 0, len(tr))
test_cases.close()
