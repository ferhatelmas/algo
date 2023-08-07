class Solution:
    def finalString(self, s: str) -> str:
        res = []
        for e in s:
            if e == "i":
                res = res[::-1]
            else:
                res.append(e)
        return "".join(res)
