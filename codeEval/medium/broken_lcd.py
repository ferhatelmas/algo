import sys

lcd_len, converter = (
    12,
    [
        "11111100",
        "01100000",
        "11011010",
        "11110010",
        "01100110",
        "10110110",
        "10111110",
        "11100000",
        "11111110",
        "11110110",
    ],
)


def bitr(n):
    r = []
    for w in n:
        if w == ".":
            if r:
                r[-1] = r[-1][:-1] + "1"
            else:
                r.append(converter[0][:-1] + "1")
        else:
            r.append(converter[int(w)])
    return r, len(r)


def is_showable(ls, n):
    rs, r_len = bitr(n)
    return any(
        all(x >= y for a, b in zip(ls[i:], rs) for x, y in zip(a, b))
        for i in xrange(lcd_len - r_len)
    )


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        bits, n = test.rstrip().split(";")
        print int(is_showable(bits.split(), n))
