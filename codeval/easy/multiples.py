import sys

def bigger(x, n):
  nl = n
  while x > n:
    n += nl
  return n 

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  x, n = map(int, test.strip().split(","))
  print bigger(x, n)
test_cases.close()