class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return str(num).rstrip("0")
