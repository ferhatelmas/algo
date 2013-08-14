import sys

ls = [(1000, "M"), (500, "D"), (100, "C"),
      (50, "L"), (10, "X"), (5, "V"), (1, "I")]
lr = [("DCCCC", "CM"), ("CCCC", "CD"), ("LXXXX", "XC"),
      ("XXXX", "XL"), ("VIIII", "IX"), ("IIII", "IV")]
def roman(n):
  r = []
  for k, v in ls:
    i = n//k
    r.append(v*i)
    n -= k*i
  r = "".join(r)
  for a, b in lr:
    r = r.replace(a, b)
  return r


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print roman(int(test))
test_cases.close()