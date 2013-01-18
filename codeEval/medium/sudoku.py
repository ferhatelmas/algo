import sys, itertools

def is_correct(n, grid):
  c = range(1, n+1)
  for i in xrange(n):
    if c != sorted(grid[0::n]):
      return False
  return True
  
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  n, grid = test.split(";")
  print is_correct(int(n), map(int, grid.split(",")))
test_cases.close()