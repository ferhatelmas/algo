import sys

def pascal(n):
  l = []
  for i in xrange(n):
    if i == 0:
      l.append([1])
    elif i == 1:
      l.append([1, 1])
    else:
      row, lrow = [1], l[-1]
      for j in xrange(len(lrow)-1):
        row.append(lrow[j] + lrow[j+1])
      row.append(1)
      l.append(row)
  return [str(e) for sl in l for e in sl]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print " ".join(pascal(int(test)))
test_cases.close()