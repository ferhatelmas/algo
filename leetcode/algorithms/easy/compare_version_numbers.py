from itertools import izip_longest


class Solution:
    def compareVersion(self, version1, version2):
        def f(v):
            return tuple(map(int, v.split(".")))

        for a, b in izip_longest(f(version1), f(version2), fillvalue=0):
            if a != b:
                return -1 if a < b else 1
        return 0
