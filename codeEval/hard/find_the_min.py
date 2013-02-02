import sys
from collections import deque
from Queue import PriorityQueue

def generate_randoms(a, b, c, r, k):
  q, d = deque([a]), {}
  if a <= k:
    d[a] = 1
  for _ in xrange(k-1):
    v = (b*q[-1]+c)%r
    q.append(v)
    if v <= k:      
      d[v] = d[v]+1 if v in d else 1
  return q, d

def get_min(n, k, a, b, c, r):
  q, d = generate_randoms(a, b, c, r, k)
  p = PriorityQueue(k+1)
  map(lambda i: p.put(i), filter(lambda i: i not in d, xrange(k+1)))
  
  for _ in xrange(k):
    q.append(p.get())
    v = q.popleft()
    if v <= k:
      if d[v] == 1:
        del d[v]
        p.put(v)
      else:
        d[v] -= 1

  q.append(p.get())
  return q[n-1-k] if n <= 2*k+1 else q[(n-2*k-2)%(k+1)]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  n, k, a, b, c, r = map(int, test.strip().split(','))
  print get_min(n, k, a, b, c, r)
test_cases.close()