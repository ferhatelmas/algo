class Solution:
    def addDigits(self, num):
        s = str(num)
        if len(s) == 1:
            return num
        return self.addDigits(sum(int(e) for e in s))
