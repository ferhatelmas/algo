import sys
from itertools import product

p = { "0": "0", "1": "1", "2": "abc",
      "3": "def", "4": "ghi", "5": "jkl",
      "6": "mno", "7": "pqrs", "8": "tuv",
      "9": "wxyz" }

def get_numbers(num):
  ls = map(lambda e: "".join(list(e)), product(*map(lambda i: tuple(p[i]), num)))
  return ",".join(ls)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print get_numbers(test.strip())
test_cases.close()