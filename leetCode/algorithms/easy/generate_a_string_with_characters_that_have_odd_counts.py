class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2:
            return "a" * n
        return "a" * (n - 1) + "b"
