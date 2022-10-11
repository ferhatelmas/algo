class Solution:
    def countDaysTogether(self, aa: str, la: str, ab: str, lb: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def index(s):
            return sum(days[0 : int(s[:2])]) + int(s[3:])

        return max(min(index(la), index(lb)) - max(index(aa), index(ab)) + 1, 0)
