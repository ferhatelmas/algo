import sys

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print " ".join(map(lambda w: w[0].upper() + w[1:], test.split()))
test_cases.close()
