import re


class CrossWord:
    def countWords(self, board, size):
        return sum(
            map(
                lambda r: len(
                    filter(lambda m: len(m) == size, re.findall("\.{2,}", r))
                ),
                board,
            )
        )
