class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            e = matrix[x][y]
            if target == e:
                return True
            elif target > e:
                x += 1
            else:
                y -= 1
        return False
