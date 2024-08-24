class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt, l = 0, len(s)
        for i in range(l):
            for j in range(i + 1, l + 1):
                n = s[i:j].count("0")
                cnt += n <= k or (j - i - n) <= k
        return cnt
