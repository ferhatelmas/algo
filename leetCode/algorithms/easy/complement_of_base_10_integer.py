class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int("".join("0" if e == "1" else "1" for e in bin(N)[2:]), 2)
