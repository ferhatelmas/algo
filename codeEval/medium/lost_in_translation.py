import sys
from string import ascii_lowercase

a = """rbc vjnmkf kd yxyqci na rbc zjkfoscdd ew rbc ujllmcp
tc rbkso rbyr ejp mysljylc kd kxveddknmc re jsicpdrysi
de kr kd eoya kw aej icfkici re zjkr"""
b = """the public is amazed by the quickness of the juggler
we think that our language is impossible to understand
so it is okay if you decided to quit"""

m = dict(zip(a, b))
m["n"], m["u"], m["g"] = "b", "j", "v"


def diff(ss):
    return set(ascii_lowercase) - set(ss)


for k, v in zip(diff(m.keys()), diff(m.values())):
    m[k] = v


def translate(s):
    return "".join(map(lambda i: m[i], s))


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print translate(test)
test_cases.close()
