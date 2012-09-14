for _ in xrange(int(raw_input())):
  raw_input()
  n = int(raw_input())
  points = []
  for _ in xrange(n):
    (x, y) = map(int, raw_input().split())
    points.append((x, y))
  points = sorted(points, cmp=lambda (x1, y1), (x2, y2): \
    x1 - x2 if x1 != x2 else y2 - y1)

  path, x, y = 0, points[0][0], points[0][1]
  for (x1, y1) in points:
    path += ((x1-x)**2 + (y1-y)**2)**.5
    x, y = x1, y1

  print "%.2f" % path