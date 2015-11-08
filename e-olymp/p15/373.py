# TODO: tle
import re
import sys


m = {'?': '.?', '*': '.*?'}


def score(s):
    return sum(ord(e) - ord('a') + 1 for e in s)


def tr(s):
    return "(?=({}))".format(''.join(m.get(e, e) for e in s))


for ln in sys.stdin:
    p, s = ln.rstrip().split()
    res = re.findall(tr(p), s)
    print(score(min(res)) if res else -1)
