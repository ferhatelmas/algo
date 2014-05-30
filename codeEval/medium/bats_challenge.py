import sys

def get_max_bats_number(l, d, n, *ns):
    if n:
        c = sum((j-i)//d-1 for i, j in zip(ns, ns[1:]))
        c += (ns[0] - 6)//d
        c += (l-6 - ns[-1])//d
    else:
        c = (l-12)//d + 1
    return c

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print get_max_bats_number(*(int(e) for e in test.rstrip().split()))
test_cases.close()
