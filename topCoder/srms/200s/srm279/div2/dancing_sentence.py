class DancingSentence:
    def makeDancing(self, sentence):
        s, f = '', True
        for e in sentence:
            if e == ' ':
                s += e
            else:
                s += (e.upper() if f else e.lower())
                f = not f
        return s
