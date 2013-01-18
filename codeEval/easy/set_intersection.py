import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  l = test.split(";")
  l = list(set(map(int, l[0].split(","))).intersection(map(int, l[1].split(","))))
  print ",".join(map(str, sorted(l)))
test_cases.close()