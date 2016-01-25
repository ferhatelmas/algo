import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        cs, r, v = collections.Counter(s), "0", {}
        for c in s:
            cs[c] -= 1
            if v.get(c, False):
                continue
            while c < r[-1] and cs[r[-1]] > 0:
                v[r[-1]], r = False, r[:-1]
            r, v[c] = r + c, True
        return r[1:]
