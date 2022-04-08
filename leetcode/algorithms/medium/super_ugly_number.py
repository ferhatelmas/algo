class Solution:
    def nthSuperUglyNumber(self, n, primes):
        u, l = [1], 1
        idx = [0] * len(primes)
        while l < n:
            nu = min(u[idx[i]] * p for i, p in enumerate(primes))
            for i, p in enumerate(primes):
                if nu == u[idx[i]] * p:
                    idx[i] += 1
            u.append(nu)
            l += 1
        return u[n - 1]
