import sys

def get_palindromic_ranges(l, r):
  ls = []
  for e in xrange(l, r+1):
    s = str(e)
    ls.append(1 if s == s[::-1] else 0)
  
  ll, cnt = len(ls), 0
  for i in xrange(ll):
    for j in xrange(i, ll):
      if sum(ls[i:j+1])%2 == 0:
        cnt += 1
  return cnt

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  l, r = map(int, test.strip().split())
  print get_palindromic_ranges(l, r)
test_cases.close()