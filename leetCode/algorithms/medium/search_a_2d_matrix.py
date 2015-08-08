class Solution:
    def searchMatrix(self, matrix, target):
        i, j, r = 0, len(matrix[0]) - 1, len(matrix)
        while i < r and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False
