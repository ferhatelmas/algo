import sys


def happy(n):
    s = set()
    while True:
        if n == 1:
            return True
        elif n in s:
            return False
        s.add(n)
        n = sum(map(lambda x: int(x) ** 2, str(n)))


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    if happy(int(test)):
        print "1"
    else:
        print "0"
test_cases.close()
