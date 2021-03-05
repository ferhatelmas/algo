import sys

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    s = test.strip().split()
    s.reverse()
    print " ".join(s)
test_cases.close()
