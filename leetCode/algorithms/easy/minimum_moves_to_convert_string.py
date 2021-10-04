class Solution:
    def minimumMoves(self, s: str) -> int:
        i, l, cnt = 0, len(s), 0
        while i < l:
            if s[i] == "O":
                i += 1
            else:
                i, cnt = i + 3, cnt + 1
        return cnt
