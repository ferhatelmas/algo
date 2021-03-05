import sys


def lsum(ls):
    l, m = len(ls), 0
    for i in xrange(l):
        for j in xrange(i + 1, l + 1):
            m = max(m, sum(ls[i:j]))
    return m


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print lsum(map(int, test.split(",")))
test_cases.close()
