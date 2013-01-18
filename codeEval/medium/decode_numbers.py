import sys
  
def decode(s):
  l = len(s)
  if l < 2:
    return 1
  res = decode(s[1:])
  if int(s[:2]) < 27:
    res += decode(s[2:])
  return res

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print decode(test.strip())
test_cases.close()