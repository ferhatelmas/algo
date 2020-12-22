class Solution:
    def reformatNumber(self, number: str) -> str:
        s = "".join(e for e in number if e not in " -")
        l = len(s)
        n = l % 3
        if n < 2:
            n += 3
        ls = []
        if l > 4:
            ls = [s[i : i + 3] for i in range(0, l - 4, 3)]
        if n == 4:
            ls.append(s[l - 4 : l - 2])
            ls.append(s[l - 2 : l])
        else:
            ls.append(s[l - n :])
        return "-".join(ls)
