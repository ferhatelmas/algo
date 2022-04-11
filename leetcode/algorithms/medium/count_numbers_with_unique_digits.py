from functools import reduce


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        def base(s, n):
            b = s[1] * (11 - n)
            return s[0] + b, b

        return reduce(base, range(2, min(n, 10) + 1), (min(10, 10**n), 9))[0]
