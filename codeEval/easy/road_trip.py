import sys

def diff(ls):
    return ','.join(map(str, [ls[0]] + [ls[i] - ls[i-1] for i in xrange(1, len(ls))]))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    ls = sorted(map(lambda e: int(e.split(',')[1]), test.strip().strip(';').split(';')))
    print diff(ls)
test_cases.close()
