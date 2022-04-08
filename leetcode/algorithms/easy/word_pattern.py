class Solution:
    def wordPattern(self, pattern, s):
        c, d = {}, {}
        ls = s.split()
        if len(ls) != len(pattern):
            return False
        for e, w in zip(pattern, ls):
            if e not in c and w not in d:
                c[e], d[w] = w, e
            elif e in c and w in d:
                if c[e] != w:
                    return False
            else:
                return False
        return True
