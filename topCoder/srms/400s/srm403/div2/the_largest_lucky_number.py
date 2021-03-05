import re


class TheLargestLuckyNumber:
    def find(self, n):
        def is_lucky(a):
            return not bool(re.search(r"[^47]", str(a)))

        while not is_lucky(n):
            n -= 1
        return n
