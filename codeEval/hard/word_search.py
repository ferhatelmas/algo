import sys

grid = [list("ABCE"), list("SFCS"), list("ADEE")]

def check_tail(w, flag, i, j):
  if len(w) == 0:
    return True
  if i>0 and flag[i-1][j] and grid[i-1][j] == w[0]:
    flag[i-1][j] = False
    if check_tail(w[1:], flag, i-1, j):
      return True
    flag[i-1][j] = True

  if i<len(grid)-1 and flag[i+1][j] and grid[i+1][j] == w[0]:
    flag[i+1][j] = False
    if check_tail(w[1:], flag, i+1, j):
      return True
    flag[i+1][j] = True

  if j>0 and flag[i][j-1] and grid[i][j-1] == w[0]:
    flag[i][j-1] = False
    if check_tail(w[1:], flag, i, j-1):
      return True
    flag[i][j-1] = True

  if j<len(grid[i])-1 and flag[i][j+1] and grid[i][j+1] == w[0]:
    flag[i][j+1] = False
    if check_tail(w[1:], flag, i, j+1):
      return True
    flag[i][j+1] = True

  return False

def exists(w):  
  for i in xrange(len(grid)):
    for j in xrange(len(grid[i])):
      if check_tail(w, [[True]*4 for _ in range(3)], i, j):
        return True
  return False

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print exists(test.strip())
test_cases.close()