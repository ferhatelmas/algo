import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print " ".join(test.split()[::-1][0::2])
test_cases.close()