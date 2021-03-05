class LeastMajorityMultiple:
    def leastMajorityMultiple(self, a, b, c, d, e):
        ls = [a, b, c, d, e]

        def is_lcm(n):
            return sum(n % j == 0 for j in ls) >= 3

        for i in xrange(1, 1000001):
            if is_lcm(i):
                return i
