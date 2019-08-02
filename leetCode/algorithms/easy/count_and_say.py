from itertools import groupby


class Solution:
    def countAndSay(self, n):
        def gen(s):
            return "".join(str(len(list(g))) + k for k, g in groupby(s))

        s, i = "1", 1
        while i < n:
            s = gen(s)
            i += 1
        return s
