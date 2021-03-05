primes = [True for _ in range(1000)]

for i in xrange(2, 1000):
    if primes[i]:
        for j in xrange(2 * i, 1000, i):
            primes[j] = False

n = 999
while True:
    if primes[n]:
        s = str(n)
        if s == s[::-1]:
            print n
            break
    n -= 1
