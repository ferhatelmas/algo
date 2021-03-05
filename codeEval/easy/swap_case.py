import sys

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print test.strip().swapcase()
test_cases.close()
