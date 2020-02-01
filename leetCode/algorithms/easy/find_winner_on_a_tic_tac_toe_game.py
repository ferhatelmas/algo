from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a = set(tuple(m) for m in moves[0::2])
        b = set(tuple(m) for m in moves[1::2])
        rows = [set((i, j) for j in range(3)) for i in range(3)]
        cols = [set((j, i) for j in range(3)) for i in range(3)]
        diag = [set([(0, 0), (1, 1), (2, 2)]), set([(2, 0), (1, 1), (0, 2)])]
        for winner in rows + cols + diag:
            if winner <= a:
                return "A"
            elif winner <= b:
                return "B"
        return ("Pending", "Draw")[len(moves) == 9]
