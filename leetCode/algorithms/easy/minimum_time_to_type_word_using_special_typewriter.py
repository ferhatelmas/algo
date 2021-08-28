class Solution:
    def minTimeToType(self, word: str) -> int:
        cur, total = ord("a"), 0
        for e in word:
            v = ord(e)
            cur, total = v, total + min((cur - v + 26) % 26, (v - cur + 26) % 26) + 1
        return total
