from itertools import zip_longest


class Solution:
    def reformat(self, s: str) -> str:
        letters, digits = [], []
        ll, ld = 0, 0
        for e in s:
            if "0" <= e <= "9":
                ld += 1
                digits.append(e)
            else:
                ll += 1
                letters.append(e)
        if abs(ll - ld) > 1:
            return ""

        short, long = letters, digits
        if ld < ll:
            short, long = long, short

        return long[0] + "".join(
            a + b for a, b in zip_longest(short, long[1:], fillvalue="")
        )
