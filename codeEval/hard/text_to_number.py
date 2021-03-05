import sys

d = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}


def get_val(ls):
    return sum([d[e] for e in ls])


def get_number(ls):
    if not ls:
        return 0
    r, f, i = 0, False, 0
    if ls[0] == "negative":
        f, i = True, 1
    for e, v in [("million", 10 ** 6), ("thousand", 10 ** 3), ("hundred", 10 ** 2)]:
        if e in ls[i:]:
            j = ls[i:].index(e)
            r += get_number(ls[i : i + j]) * v
            i += j + 1
    r += get_val(ls[i:])
    return -r if f else r


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print get_number(test.strip().split())
test_cases.close()
