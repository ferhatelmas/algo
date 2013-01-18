import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print bin(int(test))[2:].count("1")
test_cases.close()