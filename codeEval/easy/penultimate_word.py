import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  ls = test.strip().split()
  print len(ls) >= 2 and ls[-2] or ""
test_cases.close()