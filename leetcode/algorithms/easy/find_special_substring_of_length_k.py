class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        l = len(s)
        for i in range(l - k + 1):
            if i > 0 and s[i] == s[i - 1]:
                continue
            if i + k < l and s[i] == s[i + k]:
                continue
            if all(e == s[i] for e in s[i : i + k]):
                return True
        return False
