import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  if test.strip() != '':
    s, ns = test.strip().split("|")
    print "".join([s[n-1] for n in map(int, ns.split())])
test_cases.close()