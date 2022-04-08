class Solution:
    def freqAlphabets(self, s: str) -> str:
        ls, a, i, l = [], ord("a"), 0, len(s)
        while i < l:
            if s[i + 2 : i + 3] == "#":
                ls.append(chr(a + int(s[i : i + 2]) - 1))
                i += 3
            else:
                ls.append(chr(a + int(s[i]) - 1))
                i += 1
        return "".join(ls)
