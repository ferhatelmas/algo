import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
n, i = int(lines[0]), 0
for l in sorted(lines[1:], key=len, reverse=True):
  if i == n:
    break
  print l.strip()
  i += 1
f.close()