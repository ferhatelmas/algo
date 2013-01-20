import sys

def p(r, c, ls):
  b = [[True]*c for _ in range(r)]

  i, j, cnt, res = 0, -1, 0, []
  while cnt < r*c:
    while j < c-1 and b[i][j+1]:
      j += 1
      b[i][j] = False
      cnt += 1
      res.append(ls[i*c+j])

    while i < r-1 and b[i+1][j]:
      i += 1
      b[i][j] = False
      cnt += 1
      res.append(ls[i*c+j])

    while j > 0 and b[i][j-1]:
      j -= 1
      b[i][j] = False
      cnt += 1
      res.append(ls[i*c+j])
  
    while i > 0 and b[i-1][j]:
      i -= 1
      b[i][j] = False
      cnt += 1
      res.append(ls[i*c+j])
    
  return " ".join(res)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  r, c, e = test.strip().split(";")
  print p(int(r), int(c), e.split())
test_cases.close()