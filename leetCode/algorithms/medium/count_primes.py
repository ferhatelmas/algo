class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        for i in xrange(2, n):
            if primes[i]:
                for j in xrange(2 * i, n, i):
                    primes[j] = False
        return sum(primes[2:])
