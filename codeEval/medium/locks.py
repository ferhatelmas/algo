import sys

def get_open_doors(n, m):
    ls, is_odd = [True]*n, m%2 == 1
    if m > 1:
      for i in xrange(1, n+1):
        if i%3 > 0 and i%2 == 0:
          ls[i-1] = False
        elif i%3 == 0 and i%2 == 1:
          ls[i-1] = is_odd

    ls[-1] = not ls[-1]
    return sum(ls)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print get_open_doors(*map(int, test.rsplit()))
test_cases.close()
