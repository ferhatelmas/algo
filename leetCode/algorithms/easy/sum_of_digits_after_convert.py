from string import ascii_lowercase


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = "".join(str(ascii_lowercase.index(e) + 1) for e in s)
        for i in range(k):
            n = sum(int(e) for e in n)
            if n < 10:
                break
            n = str(n)
        return int(n)
