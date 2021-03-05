import sys


def reverse(n):
    return int(str(n)[::-1])


def is_palindrome(n):
    return n == reverse(n)


def reverse_add(n):
    i, n = 1, n + reverse(n)
    while not is_palindrome(n):
        i += 1
        n += reverse(n)
    print "%d %d" % (i, n)


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    reverse_add(int(test))
test_cases.close()
