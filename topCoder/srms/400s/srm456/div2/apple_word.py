class AppleWord:
    def minRep(self, word):
        if len(word) >= 5:
            c = 0
            if word[0] not in 'Aa':
                c += 1
            if word[-2] not in 'Ll':
                c += 1
            if word[-1] not in 'Ee':
                c += 1
            return c + sum(i not in 'Pp' for i in word[1:-2])
        return -1
