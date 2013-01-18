import sys
def describe(n):
  s = str(n)
  for i in xrange(0, len(s)):
    if s.count(str(i)) != int(s[i]):
      return False
  return True

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  if describe(int(test)):
    print "1"
  else:
    print "0"
test_cases.close()