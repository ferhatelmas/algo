import sys


def do_search(s, r):
    if r == "":
        return True
    for i in xrange(len(s)):
        if r[0] == "\\" and len(r) >= 2 and r[1] == "*":
            if s[i] == "*" and do_search(s[i + 1 :], r[2:]):
                return True
        elif r[0] == "*":
            if any(
                [
                    do_search(s[i + 1 :], r),
                    do_search(s[i + 1 :], r[1:]),
                    do_search(s[i:], r[1:]),
                ]
            ):
                return True
        else:
            if s[i] == r[0] and do_search(s[i + 1 :], r[1:]):
                return True
    return False


def search(s, r):
    return "true" if do_search(s, r) else "false"


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    s, r = test.strip().split(",")
    print search(s, r)
test_cases.close()
