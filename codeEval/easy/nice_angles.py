import sys

def convert(t):
    d = 1 / 60.0
    m = int(t / d)
    s = int((t - m * d) / d**2)
    return '{:02}\'{:02}"'.format(m, s)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    d, m = test.rstrip().split('.')
    print '{}.{}'.format(d, convert(float('.' + m)))
test_cases.close()
