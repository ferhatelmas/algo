class Chessboard:
    def changeNotation(self, cell):
        try:
            n = int(cell) - 1
            return chr(n % 8 + ord("a")) + str(n / 8 + 1)
        except:
            return (int(cell[1]) - 1) * 8 + ord(cell[0]) - ord("a") + 1
