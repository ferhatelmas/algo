from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        cnt = 0
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c != "R":
                    continue
                k = j + 1
                while k < 8 and r[k] == ".":
                    k += 1
                cnt += k < 8 and r[k] == "p"

                k = j - 1
                while k > -1 and r[k] == ".":
                    k -= 1
                cnt += k > -1 and r[k] == "p"

                k = i + 1
                while k < 8 and board[k][j] == ".":
                    k += 1
                cnt += k < 8 and board[k][j] == "p"

                k = i - 1
                while k > -1 and board[k][j] == ".":
                    k -= 1
                cnt += k > -1 and board[k][j] == "p"
        return cnt
