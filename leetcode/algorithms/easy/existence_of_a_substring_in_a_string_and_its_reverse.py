class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        r, l = s[::-1], len(s)
        return any(s[i : i + 2] in r for i in range(0, l - 1))
