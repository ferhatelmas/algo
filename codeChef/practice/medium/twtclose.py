n, k = map(int, raw_input().split())
ls = [False] * n
for _ in xrange(k):
  s = raw_input()
  if s.startswith('CLICK'):
    i = int(s.split()[1]) - 1
    ls[i] = not ls[i]
  else:
    ls = [False] * n
  print sum(ls)