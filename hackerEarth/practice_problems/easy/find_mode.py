from collections import Counter


for _ in xrange(int(raw_input())):
    raw_input()
    c = Counter(raw_input().rstrip().split())
    m = max(c.values())
    res = (k for k, v in c.items() if v == m)
    print(" ".join(sorted(res, reverse=True, key=int)))
