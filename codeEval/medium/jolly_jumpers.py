import sys


def jolly(ls):
    s, l = set(), len(ls)
    for i in xrange(0, l - 1):
        diff = abs(ls[i] - ls[i + 1])
        if diff >= l or diff == 0 or diff in s:
            return "Not jolly"
        else:
            s.add(diff)
    return "Jolly"


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print jolly(map(int, test.split()[1:]))
test_cases.close()
