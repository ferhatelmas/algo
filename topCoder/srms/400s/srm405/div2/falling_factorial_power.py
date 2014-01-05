from operator import div, mul

class FallingFactorialPower:
    def compute(self, n, k):
        if k > 0:
            return reduce(mul, range(n-k+1, n+1))
        return reduce(div, range(n+1, n-k+1), 1.0)
