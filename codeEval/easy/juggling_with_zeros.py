import sys

def convert(ls):
    return ''.join(ls[i+1] if ls[i] == '0' else ls[i+1].replace('0', '1')
                   for i in xrange(0, len(ls), 2))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print int(convert(test.rstrip().split()), 2)
test_cases.close()
