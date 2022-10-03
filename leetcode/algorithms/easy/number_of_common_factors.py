class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum(a % e == 0 and b % e == 0 for e in range(1, min(a, b) + 1))
