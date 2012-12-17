import sys

cache = {}

def lcs(n, m):
  if len(n) == 0 or len(m) == 0:
    return ""
  k = n + m
  if k in cache:
    return cache[n+m]
  s = n[0] if n[0] == m[0] else "" 
  cache[k] = sorted([lcs(n[1:], m), lcs(n, m[1:]), s + lcs(n[1:], m[1:])], key=len)[2]
  return cache[k]
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  if test.strip() != "":
    n, m = test.split(";")
    cache = {}
    print lcs(n, m)
test_cases.close()