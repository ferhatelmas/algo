class Solution:
    def minutes(self, s: str) -> int:
        h, m = s.split(":")
        return int(h) * 60 + int(m)

    def convertTime(self, current: str, correct: str) -> int:
        d = abs(self.minutes(current) - self.minutes(correct))
        n = 24 if current > correct else 0
        for i in (60, 15, 5):
            a, d = divmod(d, i)
            n += a
        return n + d
