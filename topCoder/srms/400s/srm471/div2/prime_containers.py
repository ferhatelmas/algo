class PrimeContainers:
    def containerSize(self, N):
        def is_prime(n):
            return not any(n%i == 0 for i in xrange(2, int(n**.5)+1))
        i, ls = 1, []
        while 2*i <= N:
            ls.append(N//i)
            i *= 2
        return sum(map(is_prime, ls))
