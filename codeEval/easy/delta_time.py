import sys


def get_diff(t1, t2):
    total_seconds = abs(
        sum((a - b) * 60 ** (2 - i) for i, (a, b) in enumerate(zip(t1, t2)))
    )
    hours, rem = divmod(total_seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:02}:{:02}:{:02}".format(*map(int, (hours, minutes, seconds)))


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print get_diff(*(map(int, e.split(":")) for e in test.rstrip().split()))
test_cases.close()
