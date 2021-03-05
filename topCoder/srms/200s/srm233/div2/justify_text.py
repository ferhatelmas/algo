class JustifyText:
    def format(self, text):
        m = max(map(len, text))
        return map(lambda s: " " * (m - len(s)) + s, text)
