import sys

romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def my_sum(ls):
    s, l = 0, len(ls)
    for i, e in enumerate(ls):
        s += int(e[0]) * romans[e[1]] * (-1 if i < l-1 and romans[e[1]] < romans[ls[i+1][1]] else 1)
    return s

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print my_sum([test[i:i+2] for i in xrange(0, len(test.rstrip()), 2)])
test_cases.close()
