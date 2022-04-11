class Solution:
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        ls, i, j = [[] for _ in range(nRows)], 0, 1
        for e in s:
            ls[i].append(e)
            i += j
            if i == nRows - 1:
                j = -1
            elif i == 0:
                j = 1
        return "".join("".join(l) for l in ls)
