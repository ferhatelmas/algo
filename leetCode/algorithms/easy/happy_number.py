class Solution:
    def c(self, s):
        return sum(int(e)**2 for e in str(s))

    def isHappy(self, n):
        seen, n = {1}, self.c(n)
        while n not in seen:
            seen.add(n)
            n = self.c(n)
        return n == 1
