import sys
from collections import Counter


def isMatch(e, c):
    d = Counter(e)
    return all(d[k] >= v for k, v in c.items())


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        wines, letters = test.rstrip().split('|')
        c = Counter(letters.strip())
        r = [e for e in wines.split() if isMatch(e, c)]
        if r:
            print(' '.join(r))
        else:
            print('False')
