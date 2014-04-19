import sys
from operator import itemgetter
from itertools import izip_longest

def recover(ls):
    return ' '.join(w for w, _ in sorted(ls, key=itemgetter(1)))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    t = [e.split() for e in test.rstrip().split(';')]
    tl, t[1] = map(len, t), map(int, t[1])
    print recover(izip_longest(t[0], t[1],
                               fillvalue=next(i for i in range(1, tl[0]+1) if i not in t[1])))
test_cases.close()
