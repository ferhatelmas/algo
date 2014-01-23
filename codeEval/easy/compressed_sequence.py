import sys
from itertools import groupby

def compress(ls):
    return ' '.join(['{} {}'.format(len(list(g)), k)
                     for k, g in groupby(ls)])

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print compress(test.rstrip().split())
test_cases.close()
