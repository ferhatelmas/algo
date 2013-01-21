import sys

def subst(s, ls):
  if s == "":
    return ""

  for j in xrange(0, len(ls), 2):
    i = s.find(ls[j])
    if i != -1:
      return subst(s[:i], ls) + ls[j+1] + subst(s[i+len(ls[j]):], ls)
  return s

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  s, sub = test.strip().split(";")
  print subst(s, sub.split(","))  
test_cases.close()