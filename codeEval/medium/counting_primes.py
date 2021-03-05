import sys


def gen_primes():
    D, q = {}, 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def count_primes(a, b):
    cnt = 0
    for p in gen_primes():
        if p >= a and p <= b:
            cnt += 1
        elif p > b:
            break
    return cnt


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    a, b = map(int, test.split(","))
    print count_primes(a, b)
test_cases.close()
