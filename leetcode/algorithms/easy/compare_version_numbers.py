from itertools import izip_longest


class Solution:
    def compareVersion(self, version1, version2):
        f = lambda v: tuple(map(int, v.split(".")))
        for a, b in izip_longest(f(version1), f(version2), fillvalue=0):
            if a != b:
                return cmp(a, b)
        return 0
