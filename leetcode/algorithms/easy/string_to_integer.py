import re


class Solution:
    def atoi(self, str):
        try:
            n = int(re.split(r"[^\d\-\+]", str.strip())[0])
            if n > 2147483647:
                return 2147483647
            elif n < -2147483648:
                return -2147483648
            return n
        except ValueError:
            return 0
