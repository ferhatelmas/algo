import sys

def get_beauty(s):
  h = {}
  for e in s:
    if e >= 'a' and e <= 'z':
      h[e] = h[e]+1 if e in h else 1
      
  vv, ss = 26, 0
  for v in sorted(h.values(), reverse=True):
    ss += v * vv
    vv -= 1
  return ss

f = open(sys.argv[1], 'r')
for l in f:
  print get_beauty(l.strip().lower())
f.close()