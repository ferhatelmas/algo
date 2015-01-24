import sys


def move(a, b):
    x, y, r = ord(a), int(b), []
    for i in (-2, -1, 1, 2):
        for j in (-2, -1, 1, 2):
            if abs(abs(i) - abs(j)) == 1:
                if ord('a') <= x + i <= ord('h') and 1 <= y + j <= 8:
                    r.append(chr(x + i) + str(y + j))
    return ' '.join(r)


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print move(*list(test.rstrip()))
