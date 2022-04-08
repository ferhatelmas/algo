class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(len(set(s[i : i + 3])) == 3 for i in range(0, len(s) - 2))
