class Solution:
    BASE = 1000000007

    def perm(self, n: int) -> bool:
        res = 1
        for i in range(n, 1, -1):
            res = (res * i) % Solution.BASE
        return res

    def numPrimeArrangements(self, n: int) -> int:
        primes = [True] * (n + 1)
        cnt = 0
        for i in range(2, n + 1):
            if not primes[i]:
                continue
            cnt += 1
            for j in range(i * 2, n + 1, i):
                primes[j] = False
        return (self.perm(cnt) * self.perm(n - cnt)) % Solution.BASE
