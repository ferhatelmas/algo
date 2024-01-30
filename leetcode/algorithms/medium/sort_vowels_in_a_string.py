class Solution:
    def sortVowels(self, s: str) -> str:
        v = set("aeiouAEIOU")
        ls, i, cs = [], 0, sorted(e for e in s if e in v)
        for e in s:
            if e in v:
                ls.append(cs[i])
                i += 1
            else:
                ls.append(e)
        return "".join(ls)
