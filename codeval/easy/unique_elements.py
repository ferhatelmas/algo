import sys, itertools

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print ",".join([k for k, _ in itertools.groupby(test.strip().split(","))])
test_cases.close()