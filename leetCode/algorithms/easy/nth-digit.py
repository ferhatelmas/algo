class Solution(object):
    def findNthDigit(self, n):
        base, mul, start = 1, 9, 1
        while n > base * mul:
            n -= base * mul
            base, mul, start = base + 1, mul * 10, start * 10
        n -= 1
        return int(str(start + n / base)[n % base])
