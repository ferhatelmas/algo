class WritingWords:
    def write(self, word):
        return sum(ord(e) - ord("A") + 1 for e in word)
