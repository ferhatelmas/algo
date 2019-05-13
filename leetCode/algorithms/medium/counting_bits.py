class Solution:
    def countBits(self, num):
        r = [0]
        for i in range(1, num + 1):
            r.append(r[i / 2] + i % 2)
        return r
