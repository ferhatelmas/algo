from math import log


def f(n):
    p = int(log(n, 2))
    c = n - 2 ** p

    s = "2(" if p != 1 else "2"
    if p >= 2:
        s += f(p)
    elif p == 0:
        s += str(p)
    s += ")" if p != 1 else ""

    if c > 0:
        s += "+" + f(c)
    return s


numbers = [137, 1315, 73, 136, 255, 1384, 16385]
for n in numbers:
    print "%d=%s" % (n, f(n))
