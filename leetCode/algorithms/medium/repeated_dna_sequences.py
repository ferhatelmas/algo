from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s):
        c = Counter(s[i:i+10] for i in range(0, len(s) - 9))
        return [k for k, v in c.items() if v > 1]
