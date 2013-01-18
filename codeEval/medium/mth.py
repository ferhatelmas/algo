import sys, string

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  l = test.split()
  s, i = len(l), int(l[-1])
  if s-1 >= i:
    print l[s-i-1]
test_cases.close()