class Inchworm:
    def lunchtime(self, branch, rest, leaf):
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        return branch / (rest * leaf / gcd(rest, leaf)) + 1
