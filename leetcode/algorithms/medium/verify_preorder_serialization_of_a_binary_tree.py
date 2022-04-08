import re


class Solution:
    def isValidSerialization(self, preorder):
        s = re.sub(r"\d+,#,#", "#", preorder)
        return s == "#" or (s != preorder and self.isValidSerialization(s))
