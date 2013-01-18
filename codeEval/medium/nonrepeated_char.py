import sys

def nonrepeat(s):
  for c in s:
    if s.count(c) == 1:
      return c

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print nonrepeat(test)
test_cases.close()