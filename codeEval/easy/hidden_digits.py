import sys


def unhide(s):
    r = ""
    for e in s:
        if "a" <= e <= "j":
            r += str(0 + ord(e) - ord("a"))
        elif "0" <= e <= "9":
            r += e
    return r if r else "NONE"


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print unhide(test)
test_cases.close()
