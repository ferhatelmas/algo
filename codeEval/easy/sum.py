import sys

test_cases = open(sys.argv[1], 'r')
print sum(map(int, test_cases))
test_cases.close()