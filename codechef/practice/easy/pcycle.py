n = int(raw_input())
p = [0] + map(int, raw_input().split())
m, c, s, cs = range(1, n + 1), [], 1, []
while len(m) >= 0:
    if s in c:
        cs.append(" ".join(map(str, c) + [str(s)]))
        c = []
        if len(m) == 0:
            break
        s = m[0]

    c.append(s)
    m.remove(s)
    s = p[s]
print len(cs)
for c in cs:
    print c
