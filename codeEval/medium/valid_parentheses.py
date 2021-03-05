import sys


def valid(s):
    l = []
    for e in s:
        if e in "({[":
            l.append(e)
        else:
            if len(l) == 0 or ")}]".index(e) != "({[".index(l.pop()):
                return False

    if len(l) != 0:
        return False
    return True


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print valid(test.strip())
test_cases.close()
