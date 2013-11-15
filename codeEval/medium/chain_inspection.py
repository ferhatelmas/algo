import sys

def is_good(ps):
    v, k = set(), 'BEGIN'
    while True:
        if k in v: return False
        elif k == 'END': break
        v.add(k)
        k = ps[k]
    return len(ps) == len(v)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print('GOOD' if is_good(dict(p.split('-')
                                 for p in test.rstrip().split(';'))) else 'BAD')
test_cases.close()
