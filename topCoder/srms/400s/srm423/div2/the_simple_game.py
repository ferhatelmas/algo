class TheSimpleGame:
    def count(self, n, x, y):
        return sum(
            min(
                i - 1 + j - 1,
                n - i + n - j,
                i - 1 + n - j,
                n - i + j - 1,
            )
            for i, j in zip(x, y)
        )
