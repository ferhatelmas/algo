import sys

cache = {}

def count(x, z):
  if len(z) < 2:
    return x.count(z)  
  k = x + ',' + z
  if k in cache:
    return cache[k]
  s = 0
  for i in xrange(len(x)):
    if x[i] == z[0]:
      s += count(x[i+1:], z[1:])
  cache[k] = s
  return s
  
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  x, z = test.strip().split(',')
  print count(x, z)
test_cases.close()