from itertools import product
from string import ascii_uppercase


class SpreadsheetColumn:
    def getLabel(self, column):
        if column < 27:
            return ascii_uppercase[column - 1]

        for c, w in enumerate(product(ascii_uppercase, repeat=2), 27):
            if c == column:
                return "".join(w)
