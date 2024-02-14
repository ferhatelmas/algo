class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2**32
        mods = list(str(i) for i in range(0, 10)) + list("abcdef")
        ls = []
        while num > 0:
            num, mod = divmod(num, 16)
            ls.append(mods[mod])
        return "".join(ls[::-1])
