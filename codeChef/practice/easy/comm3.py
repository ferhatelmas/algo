def dist(x1, y1, x2, y2):
  return ((y2-y1)**2 + (x2-x1)**2)**0.5

for _ in xrange(int(raw_input())):
  r = int(raw_input())
  a, b = map(int, raw_input().split())
  c, d = map(int, raw_input().split())
  e, f = map(int, raw_input().split())

  l = [dist(a, b, c, d), dist(a, b, e, f), dist(c, d, e, f)]
  if sorted(l)[1] <= r:
    print 'yes'
  else:
    print 'no'