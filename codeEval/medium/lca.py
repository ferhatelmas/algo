import sys

tree = [30, 52, 8, 3, 20, 10, 29]


def lca(m, n):
    i, j = sorted([tree.index(m), tree.index(n)])
    if i % 2 == 0:
        return tree[i]
    else:
        return tree[i - 1]


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    m, n = map(int, test.split())
    print lca(m, n)
test_cases.close()
