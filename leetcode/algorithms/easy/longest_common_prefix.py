class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        ls = []
        for i, e in enumerate(min(strs, key=len)):
            if [s for s in strs if s[i] != e]:
                break
            ls.append(e)
        return "".join(ls)
