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


def get_primes(n):
    l = []
    for p in gen_primes():
        if p >= n:
            break
        l.append(str(p))
    return ",".join(l)


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print get_primes(int(test))
test_cases.close()
