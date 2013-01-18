import sys

def index(s, c):
  s.reverse()
  if c in s:
    return len(s)-s.index(c)-1
  else:
    return -1

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  s, c = test.strip().split(",")
  print index(list(s), c)
test_cases.close()