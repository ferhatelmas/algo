import sys


def grab(w, ls):
    ls = map(lambda (a, b, c): (int(a), float(b), int(c[1:])), ls)
    d = {"": (0, 0)}
    for i, e in enumerate(ls):
        nd = dict()
        for k, v in d.iteritems():
            if e[1] + v[1] <= w:
                nd[k + "1"] = (e[2] + v[0], e[1] + v[1])
            nd[k + "0"] = v
        d = nd
    k = sorted(d.items(), key=lambda (k, (v, w)): (-v, w))[0][0]
    r = [str(i + 1) for i, e in enumerate(k) if e == "1"]
    return ",".join(r) if r else "-"


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    if test.strip():
        t = test.strip().split(":")
        print grab(int(t[0]), map(lambda e: e.strip("()").split(","), t[1].split()))
test_cases.close()
