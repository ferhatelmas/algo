import sys

def get_lowest_index(ns):
  for n in "123456789":
    if ns.count(n) == 1:
      return ns.index(n) + 1
  return 0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print get_lowest_index(test.split())
test_cases.close()