class NumArray(object):
    def __init__(self, nums):
        self.s = []
        for i, e in enumerate(nums):
            self.s.append(e + (self.s[i - 1] if i > 0 else 0))

    def sumRange(self, i, j):
        n = self.s[j]
        if i > 0:
            n -= self.s[i - 1]
        return n
