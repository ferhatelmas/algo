from collections import Counter


class Solution:
    def isValidSudoku(self, board):
        def is_valid(it):
            print it
            t = tuple(e for e in it if e != '.')
            if t:
                return max(Counter(t).values()) < 2
            return True
        return (all(is_valid(r) for r in board) and
                all(is_valid(c) for c in zip(*board)) and
                all(is_valid(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3])
                    for i in (0, 3, 6) for j in (0, 3, 6)))
