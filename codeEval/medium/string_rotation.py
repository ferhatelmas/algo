import sys


def rotation(ls):
    s = ls[0] + ls[0]
    return s.find(ls[1]) == -1


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print(rotation(test.strip().split(",")))
test_cases.close()
