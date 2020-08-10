class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s, c = "0", 1
        while c < n:
            s = s + "1" + "".join("1" if e == "0" else "0" for e in reversed(s))
            c += 1
        return s[k - 1]
