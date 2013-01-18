import sys, re

test_cases = open(sys.argv[1], 'r')
for test in map(lambda x: x.strip(), test_cases):
  if test != "":
    if re.search('^([0-9a-zA-Z]([-\.\w]*[0-9a-zA-Z])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})$', test, re.I):
      print "true"
    else:
      print "false"
test_cases.close()