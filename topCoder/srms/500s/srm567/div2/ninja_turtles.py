class NinjaTurtles:
    def countOpponents(self, P, K):
        n = 3 * P * K / (K + 9)
        c = n / 3 + 3 * (n / K)
        while c < P:
            n += 1
            c = n / 3 + 3 * (n / K)
        return n if c == P else -1
