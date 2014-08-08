import sys
from string import ascii_letters

def roll(ls):
    res, f = [], True
    for e in ls:
      if e in ascii_letters:
        if f:
          res.append(e.upper())
        else:
          res.append(e.lower())
        f = not f
      else:
        res.append(e)
    return ''.join(res)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print roll(test.rstrip())
test_cases.close()
