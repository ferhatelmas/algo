class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = len(s)
        res = ["a"] * l
        for i, e in enumerate(s[: l // 2 + 1]):
            w = s[l - i - 1]
            if e != w:
                if e > w:
                    e = w
            res[i] = res[l - i - 1] = e
        return "".join(res)
