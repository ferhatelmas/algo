import sys


a = "A | B | C | D | E | F | G | H | I | J | K | L | M"
b = "U | V | W | X | Y | Z | N | O | P | Q | R | S | T"
c = {}


def clean(s):
    return [e.strip().lower() for e in s.split("|")]


for i, j in zip(clean(a), clean(b)):
    c[i], c[j] = j, i


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print("".join(c[e] for e in test.rstrip()))
