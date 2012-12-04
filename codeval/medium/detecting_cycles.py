import sys, itertools

def grouper(n, iterable, fillvalue=None):    
  args = [iter(iterable)] * n
  return itertools.izip_longest(fillvalue=fillvalue, *args)

def detect_cycle(ls):
  l = len(ls)
  for i in xrange(l-1):
    for j in xrange((l-i)/2, 0, -1):
      s = set(grouper(j, ls[i:], 'x'))
      if len(s) == 1:
        print " ".join(s.pop())
        return
  
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  detect_cycle(test.split())
test_cases.close()