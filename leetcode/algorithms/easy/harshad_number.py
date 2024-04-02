class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = sum(int(e) for e in str(x))
        return n if x % n == 0 else -1
