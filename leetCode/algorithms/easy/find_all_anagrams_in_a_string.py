from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        lp, ls = len(p), []
        sc, pc, p = Counter(s[: lp - 1]), Counter(p), 0
        for i, c in enumerate(s[lp - 1 :], start=lp - 1):
            sc[c] += 1
            if sc == pc:
                ls.append(p)
            sc[s[p]] -= 1
            if sc[s[p]] == 0:
                del sc[s[p]]
            p += 1
        return ls
