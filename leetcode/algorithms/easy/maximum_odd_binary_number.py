class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        o, z = 0, 0
        for e in s:
            if e == "1":
                o += 1
            else:
                z += 1
        return "1" * (o - 1) + "0" * z + "1"
