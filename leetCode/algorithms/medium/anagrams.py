from collections import defaultdict

class Solution:
    def anagrams(self, strs):
        d = defaultdict(list)
        res = []
        for s in strs:
            d[''.join(sorted(s))].append(s)
        for k in d:
            if len(d[k]) > 1:
                res.extend(d[k])
        return res