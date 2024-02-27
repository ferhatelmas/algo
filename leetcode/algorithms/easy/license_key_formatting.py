class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ls = []
        for e in s:
            if e != "-":
                ls.append(e.upper())
        l = len(ls)
        first = l % k
        res = []
        if first > 0:
            res.append("".join(ls[:first]))
        for i in range(first, l, k):
            res.append("".join(ls[i : i + k]))
        return "-".join(res)
