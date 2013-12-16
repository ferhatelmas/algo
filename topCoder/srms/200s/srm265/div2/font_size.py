class FontSize:
    def getPixelWidth(self, sentence, uppercase, lowercase):
        l = 0
        for e in sentence:
            if e == ' ':
                l += 3
            elif 'A' <= e <= 'Z':
                l += uppercase[ord(e) - ord('A')]
            else:
                l += lowercase[ord(e) - ord('a')]
            l += 1
        return l-1 if sentence else l
