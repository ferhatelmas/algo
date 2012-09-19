'''
Correct but time limit, notatri.cpp is ok
'''
n = int(raw_input())
while(n != 0):
  p = sorted(map(int, raw_input().split()))
  cnt = 0
  for i in xrange(n-1, 1, -1):
    b, e = 0, i-1
    while(b < e):
      if(p[i] > p[e] + p[b]):
        cnt += e-b
        b += 1
      else:
        e -= 1 
  print(cnt)
  n = int(raw_input())