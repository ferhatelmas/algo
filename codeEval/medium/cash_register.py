import sys

coins = {.01:"PENNY", .05:"NICKEL", .1:"DIME", .25:"QUARTER", .5:"HALF DOLLAR", 
1.: "ONE", 2.:"TWO", 5.:"FIVE", 10.:"TEN", 20.:"TWENTY", 50.:"FIFTY", 100.:"ONE HUNDRED"}

def register(n):
  reg = []
  for c in sorted(coins.keys(), reverse=True):
    while n >= c:
      reg.append(coins[c])
      n = round(n-c, 2)
  return ",".join(sorted(reg))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  p, c = map(float, test.split(";"))
  if c < p:
    print "ERROR"
  elif c == p:
    print "ZERO"
  else:
    print register(c - p)
test_cases.close()