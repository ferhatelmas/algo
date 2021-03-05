import sys


def order(ls, l, gap):
    swapped = False
    for i in range(l - gap):
        j = i + gap
        if ls[i] > ls[j]:
            swapped = True
            ls[i], ls[j] = ls[j], ls[i]
    return swapped


def comb_sort(ls):
    l = gap = len(ls)
    c = 0
    while True:
        gap = max(int(gap / 1.25), 1)
        if not order(ls, l, gap) and gap == 1:
            return c
        c += 1


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        print(comb_sort(map(int, test.split())))
