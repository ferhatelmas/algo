class WordAbbreviation:
    def getAbbreviations(self, words):
        def shorten(w):
            for i in xrange(1, len(w)):
                if not any(e.startswith(w[:i]) for e in words if e != w):
                    return w[:i]
            return w

        return map(shorten, words)
