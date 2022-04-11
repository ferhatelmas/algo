from operator import is_


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def main():
    m = -1
    for a in range(999, 99, -1):
        for b in range(999, 99, -1):
            n = a * b
            if is_palindrome(n):
                m = max(m, n)
    return m


print(main())
