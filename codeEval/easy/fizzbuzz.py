import sys

def fizzbuzz(a, b, n):
  l = []
  for i in xrange(1, n+1):
    if i%a == 0 and i%b == 0:
      l.append("FB")
    elif i%a == 0:
      l.append("F")
    elif i%b == 0:
      l.append("B")
    else:
      l.append(str(i))
  return " ".join(l)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  a, b, n = map(int, test.split())
  print fizzbuzz(a, b, n)
test_cases.close()