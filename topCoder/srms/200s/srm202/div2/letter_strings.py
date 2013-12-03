class LetterStrings:
    def sum(self, s):
        return len(filter(lambda i: i != '-', ''.join(s)))
