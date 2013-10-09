import sys

def get_longest_word(ws):
  w, i = ws[0], len(ws[0])
  for e in ws:
    j = len(e)
    if j > i:
      w, i = e, j
  return w
  
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print get_longest_word(test.split())
test_cases.close()