class Solution:
    def toGoatLatin(self, S: str) -> str:
        res, a = [], ""
        for w in S.split():
            a += "a"
            if w[0].lower() in "aeiou":
                res.append(w + "ma" + a)
            else:
                res.append(w[1:] + w[0] + "ma" + a)
        return " ".join(res)
