from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        c = Counter(s)
        for i, e in enumerate(s):
            if c[e] == 1:
                return i
        return -1
