import re
import sys


def transform(s):
    if len(s) <= 55:
        return s
    a = s[:40]
    if re.match(r"\S.*", s[40:]):
        i = a.rfind(" ")
        if i > -1:
            a = a[:i]
    return a.rstrip(" ") + "... <Read More>"


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print transform(test.rstrip())
test_cases.close()
