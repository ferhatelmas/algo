class InsideOut:
    def unscramble(self, line):
        i = len(line) / 2
        return line[:i][::-1] + line[i:][::-1]
