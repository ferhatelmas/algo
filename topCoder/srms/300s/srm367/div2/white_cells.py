class WhiteCells:
    def countOccupied(self, board):
        return sum(
            i % 2 == j % 2 and c == "F"
            for i, r in enumerate(board)
            for j, c in enumerate(r)
        )
