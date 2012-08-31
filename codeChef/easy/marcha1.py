def is_balanced(d, m):
  if len(d) > 0 and d[0] == m:
    return True

  if len(d) > 1 and d[0] < m:
    return is_balanced(d[1:], m) or is_balanced(d[1:], m-d[0])

for _ in xrange(int(raw_input())):
  [n, m] = [int(i) for i in raw_input().split()]
  
  d = []
  for _ in xrange(n):
    i = int(raw_input())
    if i <= m:
      d.append(i)
  d.sort()
  print 'Yes' if is_balanced(d, m) else 'No'