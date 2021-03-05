import re


class TextStatistics:
    def averageLength(self, text):
        s, c = 0.0, 0
        for e in re.finditer(r"([a-zA-Z]+)", text):
            s += len(e.group(1))
            c += 1
        return s / c if c else s
