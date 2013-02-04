import sys

def minesweep(edges, f):
  (m, n), res = edges, [] 
  for i in xrange(m):
    for j in xrange(n):
      if f[i*n+j] == '.':
        r1 = xrange(max(i-1, 0), min(i+1, m-1)+1)
        r2 = xrange(max(j-1, 0), min(j+1, n-1)+1)
        res.append([f[a*n+b] for a in r1 for b in r2].count('*'))
      else:
        res.append('*')
  return "".join(map(str, res))
  
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  edges, field = test.strip().split(';')
  print minesweep(map(int, edges.split(',')), list(field))
test_cases.close()