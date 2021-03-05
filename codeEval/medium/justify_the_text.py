import sys


def adjust(s):
    ls = s.strip().split()
    l = len(ls)
    if l < 2:
        return "".join(ls)
    used = sum(len(w) for w in ls)
    needed = 80 - used
    per, rest = divmod(needed, l - 1)
    multipliers = [per + 1] * rest + [per] * (l - rest - 1) + [0]
    return "".join(w + " " * m for m, w in zip(multipliers, ls))


def justify(s):
    res, l = [], len(s)
    while l > 80:
        ln, rest = s[:80], ""
        if s[80] != " ":
            ln, rest = ln.rsplit(" ", 1)
            used = 80 - len(rest)
        else:
            used = 81
        s, l = s[used:], l - used
        res.append(adjust(ln))
    s = s.strip()
    if s:
        res.append(s)
    return "\n".join(res)


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        print justify(test.rstrip())
