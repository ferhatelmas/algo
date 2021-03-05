import sys


def pi_digits():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            q, r, t, k, n, l = (
                10 * q,
                10 * (r - n * t),
                t,
                k,
                (10 * (3 * q + r)) / t - 10 * n,
                l,
            )
        else:
            q, r, t, k, n, l = (
                q * k,
                (2 * q + r) * l,
                t * l,
                k + 1,
                (q * (7 * k + 2) + r * l) / (t * l),
                l + 2,
            )


digits = pi_digits()
pi = [digits.next() for _ in range(5000)]
with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        print(pi[int(test) - 1])
