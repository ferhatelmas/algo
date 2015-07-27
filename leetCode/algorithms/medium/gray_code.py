class Solution:
    def grayCode(self, n):
        ls = [0]
        for i in range(n):
            p, s = 1 << i, len(ls)
            while s:
                s -= 1
                v = p | ls[s]
                ls.append(v)
        return ls
