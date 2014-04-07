import sys

def get_max_chain_length(ls, c=None):
    l = 0
    for i, s1 in enumerate(ls):
        if not c or s1[0] == c:
            l = max(l, get_max_chain_length([s2 for j, s2 in enumerate(ls) if i != j], s1[-1]))
    return l+1 if c else l if l > 1 else None

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print get_max_chain_length(test.rstrip().split(','))
test_cases.close()
