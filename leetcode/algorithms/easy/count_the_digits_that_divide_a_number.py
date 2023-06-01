class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num % int(e) == 0 for e in str(num))
