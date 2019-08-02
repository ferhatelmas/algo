class Solution:
    def gameOfLife(self, board):
        cp = [[c for c in r] for r in board]
        for i, r in enumerate(cp):
            for j, c in enumerate(r):
                s = (
                    sum(
                        sum(ls[max(j - 1, 0) : j + 2])
                        for ls in cp[max(i - 1, 0) : i + 2]
                    )
                    - c
                )
                if c == 1:
                    board[i][j] = 1 if 2 <= s <= 3 else 0
                else:
                    board[i][j] = 1 if s == 3 else 0
                print(i, j, s, cp[i][j], board[i][j])
