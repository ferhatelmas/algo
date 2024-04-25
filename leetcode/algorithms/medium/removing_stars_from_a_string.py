class Solution:
    def removeStars(self, s: str) -> str:
        ls = []
        for e in s:
            if e == "*":
                ls.pop()
                continue
            ls.append(e)
        return "".join(ls)
