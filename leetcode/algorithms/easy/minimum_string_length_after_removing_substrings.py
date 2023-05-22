class Solution:
    def minLength(self, s: str) -> int:
        removed = True
        while removed:
            removed = False
            for i in range(len(s)):
                if s[i : i + 2] == "AB" or s[i : i + 2] == "CD":
                    s = s[:i] + s[i + 2 :]
                    removed = True
                    break
        return len(s)
