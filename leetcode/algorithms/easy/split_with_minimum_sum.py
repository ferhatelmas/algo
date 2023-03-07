class Solution:
    def splitNum(self, num: int) -> int:
        ls = sorted(list(str(num)))
        return int("".join(ls[::2])) + int("".join(ls[1::2]))
