catalans = [1]
for i in xrange(0, 1001):
  catalans.append((2*(2*i+1)*catalans[-1])/(i+2))

for _ in xrange(int(raw_input())):
  print catalans[int(raw_input())-1]%10000