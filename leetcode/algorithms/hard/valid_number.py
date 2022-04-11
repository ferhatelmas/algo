class Solution:
    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
