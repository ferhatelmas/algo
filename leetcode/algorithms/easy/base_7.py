class Solution:
    def convertToBase7(self, num: int) -> str:
        ls, prefix = [], ""
        if num < 0:
            num = -num
            prefix = "-"
        while num > 0:
            ls.append(str(num % 7))
            num //= 7
        return prefix + ("".join(ls[::-1]) if ls else "0")
