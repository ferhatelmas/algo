import sys, math


def squares(x):
    cnt = 0
    for i in xrange(0, int(x ** 0.5) + 1):
        y = (x - i ** 2) ** 0.5
        if y == math.trunc(y) and y >= i:
            cnt += 1
    return cnt


test_cases = open(sys.argv[1], "r")
for test in test_cases.readlines()[1:]:
    print squares(int(test))
test_cases.close()
