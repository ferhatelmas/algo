class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n + 1):
            a2 = a * a
            for b in range(1, n + 1):
                c = (a2 + b * b) ** 0.5
                cnt += c == int(c) and c <= n
        return cnt
