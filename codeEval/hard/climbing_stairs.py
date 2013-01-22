import sys

cache = {}

def count(n):
  if n <= 2:
    return n
  if n in cache:
    return cache[n]
  v = count(n-1) + count(n-2)
  cache[n] = v
  return v
  
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print count(int(test.strip()))
test_cases.close()