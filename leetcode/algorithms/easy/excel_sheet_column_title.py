class Solution:
    def convertToTitle(self, num):
        ls = []
        while num:
            num, i = divmod(num, 26)
            if i == 0 and num > 0:
                num -= 1
                i = 26
            ls.append(chr(ord("A") - 1 + i))
        return "".join(reversed(ls))
