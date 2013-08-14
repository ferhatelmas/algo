import sys

def get_max_submatrix(m):
  n, r = len(m), 0
  for i in xrange(n):
    for j in xrange(i, n):
      for k in xrange(n):
        for l in xrange(k, n):
          r = max(r, sum(map(lambda ls: sum(ls[k:l+1]), m[i:j+1])))
  return r

m = []
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  m.append(map(int, test.strip().split()))
test_cases.close()
print get_max_submatrix(m)