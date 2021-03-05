import sys

coins = {
    0.01: "PENNY",
    0.05: "NICKEL",
    0.1: "DIME",
    0.25: "QUARTER",
    0.5: "HALF DOLLAR",
    1.0: "ONE",
    2.0: "TWO",
    5.0: "FIVE",
    10.0: "TEN",
    20.0: "TWENTY",
    50.0: "FIFTY",
    100.0: "ONE HUNDRED",
}


def register(n):
    reg = []
    for c in sorted(coins.keys(), reverse=True):
        while n >= c:
            reg.append(coins[c])
            n = round(n - c, 2)
    return ",".join(sorted(reg))


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    p, c = map(float, test.split(";"))
    if c < p:
        print "ERROR"
    elif c == p:
        print "ZERO"
    else:
        print register(c - p)
test_cases.close()
