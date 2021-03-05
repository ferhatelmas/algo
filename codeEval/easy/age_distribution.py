import sys
from bisect import bisect


def distribute(age):
    s = (
        "Home",
        "Preschool",
        "Elementary school",
        "Middle school",
        "High school",
        "College",
        "Work",
        "Retirement",
        "This program is for humans",
    )
    a = [0, 3, 5, 12, 15, 19, 23, 66, 101]
    return s[bisect(a, age) - 1]


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print distribute(int(test.rstrip()))
test_cases.close()
