import sys
from itertools import permutations

def get_next(s):
    ss = sorted(s, reverse=True)
    if ''.join(ss) == s:
        non = [e for e in ss if e != '0']
        return ''.join([non[-1]] + ss[len(non):] + ['0'] + non[:-1][::-1])
    else:
        s = tuple(s)
        for p in permutations(sorted(s)):
            if p > s:
                return ''.join(p)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print get_next(test.rstrip())
test_cases.close()
