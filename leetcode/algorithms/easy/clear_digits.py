from string import digits


class Solution:
    def clearDigits(self, s: str) -> str:
        ls = []
        for e in s:
            if e in digits:
                ls.pop()
            else:
                ls.append(e)
        return "".join(ls)
