class TextCompressor:
    def longestRepeat(self, sourceText):
        l = len(sourceText)
        for i in xrange(l/2, 0, -1):
            for j in xrange(0, l-i):
                if sourceText[j:i+j] in sourceText[i+j:]:
                    return sourceText[j:i+j]
        return ''
