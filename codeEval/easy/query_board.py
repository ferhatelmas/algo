import sys, re

v = re.compile("\d+")
board = [[0] * 256 for _ in xrange(256)]


def set_row(l):
    for i in xrange(256):
        board[l[0]][i] = l[1]


def set_col(l):
    for i in xrange(256):
        board[i][l[0]] = l[1]


def sum_row(l):
    print sum(board[l[0]])


def sum_col(l):
    print sum([board[i][l[0]] for i in xrange(256)])


def query(s):
    l = map(int, v.findall(s))
    if s.startswith("SetRow"):
        set_row(l)
    elif s.startswith("SetCol"):
        set_col(l)
    elif s.startswith("QueryRow"):
        sum_row(l)
    else:
        sum_col(l)


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    query(test.strip())
test_cases.close()
