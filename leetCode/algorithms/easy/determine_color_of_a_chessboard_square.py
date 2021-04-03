class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a, b = coordinates
        n = "abcdefgh".index(a) + int(b)
        return n % 2 == 0
