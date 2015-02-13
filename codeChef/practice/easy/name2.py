from sys import stdin


def test(a, b):
    al, bl = list(a), list(b)
    while al and bl:
        if al[-1] == bl[-1]:
            al.pop()
        bl.pop()
    return not al


def is_possible(a, b):
    return test(a, b) or test(b, a)


print '\n'.join(
    ('NO', 'YES')[is_possible(*ln.split())]
    for i, ln in enumerate(stdin)
    if i
)
