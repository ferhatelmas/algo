from operator import mul

class Cryptography:
    def encrypt(self, numbers):
        def d(a, b):
            return reduce(mul, a, 1) * reduce(mul, b, 1)
        return max(d(numbers[:i], numbers[i+1:])*(e+1) for i, e in enumerate(numbers))
