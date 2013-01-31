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

f = open(sys.argv[1], 'r')
for i in range(1, int(f.readline())+1):
  n, k = map(int, f.readline().strip().split())
  a, b, c, r = map(int, f.readline().strip().split())
  print "Case #%d: %d" % (i, get_min(n, k, a, b, c, r))
f.close()