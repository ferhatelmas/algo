class Solution(object):
    def isSubsequence(self, s, t):
        ls, lt = len(s), len(t)
        if ls > lt:
            return False
        if ls == lt:
            return s == t
        j = -1
        for c in s:
            found = False
            while j < lt - 1:
                j += 1
                found = t[j] == c
                if found:
                    break
            if not found:
                return False
        return True
