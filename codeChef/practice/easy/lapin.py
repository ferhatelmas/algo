from sys import stdin


def is_lapindrome(s):
    l = len(s)
    return sorted(s[:l / 2]) == sorted(s[l / 2 + l % 2:])


for i, ln in enumerate(stdin):
    if i > 0:
        print('NO', 'YES')[is_lapindrome(ln.rstrip())]
