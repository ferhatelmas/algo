import re, sys

p = re.compile(r'(.+?)\1+?')
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = test.strip()
  try:
    print len(p.match(test).group(1))
  except:
    print len(test)
test_cases.close()