import sys, itertools

def zero_sum(ls):
  return len(filter(lambda x: sum(x) == 0, itertools.combinations(ls, 4)))
  
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print zero_sum(map(int, test.split(",")))
test_cases.close()