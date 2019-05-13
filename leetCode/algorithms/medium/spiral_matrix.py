class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        t, b, l, r, d = 0, len(matrix) - 1, 0, len(matrix[0]) - 1, 0
        res = []
        while t <= b and l <= r:
            if d == 0:
                res.extend(matrix[t][l:r + 1])
                t += 1
            elif d == 1:
                res.extend(e[r] for e in matrix[t:b + 1])
                r -= 1
            elif d == 2:
                res.extend(matrix[b][l:r + 1][::-1])
                b -= 1
            elif d == 3:
                res.extend(e[l] for e in matrix[t:b + 1][::-1])
                l += 1
            d = (d + 1) % 4
        return res
