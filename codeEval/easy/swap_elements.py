import sys

def swap(ls, ts):
  for i, j in ts:
    ls[j], ls[i] = ls[i], ls[j]
  return ' '.join(ls)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  n, t = test.split(':')
  ns = n.split()
  ts = map(lambda e: map(int, e.split('-')), t.split(','))
  print swap(ns, ts)
test_cases.close()
