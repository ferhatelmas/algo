class Solution:
    def isAdditiveNumber(self, num):
        l = len(num)
        for i in range(1, l):
            for j in range(i + 1, l):
                a = self.parse(num[:i])
                b = self.parse(num[i:j])
                if a is not None and b is not None and self.dfs(num[j:], a, b):
                    return True
        return False

    def dfs(self, s, a, b):
        if not s:
            return True
        for i in range(1, len(s) + 1):
            c = self.parse(s[:i])
            if c is not None and a + b == c and self.dfs(s[i:], b, c):
                return True
        return False

    def parse(self, s):
        if s[0] == '0' and s != '0':
            return
        return int(s)


assert Solution().isAdditiveNumber("112358")
assert Solution().isAdditiveNumber("199100199")
assert not Solution().isAdditiveNumber("1203")
assert not Solution().isAdditiveNumber("1023")
assert Solution().isAdditiveNumber("101")
