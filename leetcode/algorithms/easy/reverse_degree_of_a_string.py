from string import ascii_lowercase


class Solution:
    def reverseDegree(self, s: str) -> int:
        d = dict(zip(ascii_lowercase, range(26, 0, -1)))
        return sum(i * d[c] for i, c in enumerate(s, start=1))
