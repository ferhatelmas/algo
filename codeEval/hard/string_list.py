import sys
from itertools import product

def get_string_list(n, s):
  return ",".join(["".join(list(e)) for e in sorted(set(product(s, repeat=n)))])

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  n, s = test.strip().split(',')
  print get_string_list(int(n), s)
test_cases.close()