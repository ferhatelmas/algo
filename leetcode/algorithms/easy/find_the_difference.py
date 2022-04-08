import itertools


class Solution(object):
    def findTheDifference(self, s, t):
        for a, b in itertools.izip_longest(sorted(s), sorted(t)):
            if a != b:
                return b
