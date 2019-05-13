class Solution:
    def primes(self, n):
        d = 2
        while d * d <= n:
            c = 0
            while (n % d) == 0:
                c += 1
                n //= d
            yield (d, c)
            d += 1
        if n > 1:
            yield (n, 1)

    def numSquares(self, n):
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        if any(p % 4 == 3 and e % 2 == 1 for p, e in self.primes(n)):
            return 3
        return 1 if int(n**.5)**2 == n else 2
