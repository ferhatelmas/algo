class AlmostPrimeNumbers:
    def getNext(self, m):
        sieve = [True] * (10 ** 6 + 2)
        for i in xrange(2, 10 ** 6 + 2):
            if sieve[i]:
                for j in xrange(2 * i, 10 ** 6 + 2, i):
                    sieve[j] = False

        def is_almost(n):
            return not sieve[n] and not any(n % i == 0 for i in xrange(2, 11))

        i = m + 1
        while not is_almost(i):
            i += 1
        return i
