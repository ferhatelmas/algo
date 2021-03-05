import re
import sys
from collections import Counter

patterns = {
    "dotted_binary": (re.compile(r"((?:[01]{8}\.){3}[01]{8})"), 2),
    "dotted_octal": (re.compile(r"((?:0[0-7]{3}\.){3}0[0-7]{3})"), 8),
    "dotted_decimal": (re.compile(r"((?:\d{1,3}\.){3}\d{1,3})"), 10),
    "dotted_hex": (re.compile(r"((?:0x[a-fA-F\d]{2}\.){3}0x[a-fA-F\d]{2})"), 16),
    "plain_binary": (re.compile(r"([01]{32})"), 2),
    "plain_octal": (re.compile(r"(0[0-7]{11})"), 8),
    "plain_decimal": (re.compile(r"(\d{10})"), 10),
    "plain_hex": (re.compile(r"(0x[a-fA-F\d]{8})"), 16),
}


def convert_dotted(s, b):
    return tuple(int(e, b) for e in s.split(r"."))


def convert_plain(s, b):
    bs = "{:0>32}".format(bin(int(s, b))[2:])
    return tuple(int(bs[i * 8 : (i + 1) * 8], 2) for i in range(4))


def convert(lines):
    ips = Counter()
    for j, line in enumerate(lines, 1):
        for k, (v, b) in patterns.items():
            for l in re.findall(v, line):
                ip = globals()["convert_" + k.split("_")[0]](l, b)
                if (1, 0, 0, 0) <= ip <= (255, 255, 255, 254):
                    ips[ip] += 1

    c = ips.most_common(1)[0][1]
    return str(c), [k for k, v in ips.items() if v == c]


def format(c, ls):
    return "{}{}".format(
        c + " " if len(ls) > 1 else "",
        " ".join(".".join(map(str, e)) for e in sorted(ls)),
    )


test_cases = open(sys.argv[1], "r")
print format(*convert(test_cases))
test_cases.close()
