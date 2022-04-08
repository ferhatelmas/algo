class Solution:
    def rob(self, num):
        ls = [[0, 0]]
        for e in num:
            ls.append([max(ls[-1][0], ls[-1][1]), ls[-1][0] + e])
        return max(ls[-1])
