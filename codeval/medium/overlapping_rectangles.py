import sys

def overlap(ls):
  if max(ls[0], ls[4]) > min(ls[2], ls[6]) or max(ls[3], ls[7]) > min(ls[1], ls[5]):
    return False
  return True

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print overlap(map(int, test.split(",")))
test_cases.close()