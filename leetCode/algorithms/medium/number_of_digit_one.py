class Solution:
    def countDigitOne(self, n):
        acc, i, f, c = 0, 0, 1, 0
        while n > 0:
            n, r = divmod(n, 10)
            if r == 1:
                c += i + acc + 1
            elif r > 1:
                c += r * i + f
            acc, i, f = acc + r * f, i * 10 + f, f * 10
        return c
