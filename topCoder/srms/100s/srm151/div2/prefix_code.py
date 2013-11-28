class PrefixCode:
    def isOne(self, words):
        length = len(words)
        for i in xrange(length):
            for j in xrange(length):
                if i != j and words[j].startswith(words[i]):
                    return 'No, {}'.format(i)
        return 'Yes'
