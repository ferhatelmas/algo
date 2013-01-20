l = [[True]*4 for _ in range(4)]

def s(r, c):
  if r == 3 and c == 3:
    return 1
  elif max(r, c) > 3 or min(r, c) < 0:
    return 0
  elif not l[r][c]:
    return 0
  else:
    l[r][c] = False
    cnt = s(r+1, c) + s(r-1, c) + s(r, c+1) + s(r, c-1)
    l[r][c] = True
    return cnt

print s(0, 0)