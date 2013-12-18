class FarFromPrimes:
    def count(self, A, B):
        sieve = [True] * (B+11)
        for i in xrange(2, B+11):
            if sieve[i]:
                for j in xrange(2*i, B+11, i):
                    sieve[j] = False

        c = 0
        for i in xrange(A, B+1):
            if not any(sieve[i-10:i+11]):
                c += 1
        return c
