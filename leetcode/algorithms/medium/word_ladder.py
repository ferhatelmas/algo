import string


class Solution:
    def ladderLength(self, start, end, d):
        found, c = set([start]), 1
        d.add(end)
        while end not in found:
            new_founds = set()
            for s in found:
                for i, e in enumerate(s):
                    for ch in string.ascii_lowercase:
                        w = s[:i] + ch + s[i + 1 :]
                        if w in d:
                            new_founds.add(w)
                            d.remove(w)
            c += 1
            if not new_founds:
                return 0
            found = new_founds
        return c
