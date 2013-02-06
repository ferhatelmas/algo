import sys, re

def get_repeated_substring(s):
  l = len(s)
  for i in xrange(l/2, 0, -1):
    for j in xrange(l-i+1):
      ss = s[j:j+i]
      if not re.match('\s+', ss):
        for k in xrange(i+j, l-i+1):
          if s[k:k+i] == ss:
            return ss
  return "NONE"

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print get_repeated_substring(test.strip())
test_cases.close()