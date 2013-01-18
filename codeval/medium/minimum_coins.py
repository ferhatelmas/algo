import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  n = int(test)
  c, m = n/5, n%5
  c, m = c+m/3, m%3
  print c+m
test_cases.close()