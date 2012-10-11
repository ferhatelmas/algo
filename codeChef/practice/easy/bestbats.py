import math

for _ in xrange(int(raw_input())):
  scores, k = sorted(map(int, raw_input().split()), reverse=True), int(raw_input())
  mscores = scores[:k]
  
  n, m = mscores.count(mscores[-1]), scores.count(mscores[-1])
  print math.factorial(m)/(math.factorial(n)*math.factorial(m-n))