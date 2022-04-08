class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(len(str1), 0, -1):
            s = str1[:i]
            if str1.replace(s, "") == "" and str2.replace(s, "") == "":
                return s
        return ""
