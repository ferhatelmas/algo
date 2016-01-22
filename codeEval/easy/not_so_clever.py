import sys


def step(ls):
    for i, (a, b) in enumerate(zip(ls, ls[1:])):
        if a > b:
            ls[i], ls[i+1] = b, a
            return


def my_sort(ls, n):
    while n > 0:
        step(ls)
        n -= 1
    return " ".join(map(str, ls))


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        ls, n = test.split("|")
        print(my_sort(map(int, ls.split()), int(n)))
