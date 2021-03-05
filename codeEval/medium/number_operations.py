from itertools import permutations, product
from sys import argv


def calc(e, ops):
    v = e[0]
    for i, op in zip(e[1:], ops):
        if op == "+":
            v += i
        elif op == "-":
            v -= i
        else:
            v *= i
    return v


def is_possible(ls):
    for e in permutations(ls):
        for op in product("+-*", repeat=4):
            if calc(e, op) == 42:
                return True
    return False


with open(argv[1], "rb") as test_cases:
    for test in test_cases:
        print(("NO", "YES")[is_possible(map(int, test.split()))])
