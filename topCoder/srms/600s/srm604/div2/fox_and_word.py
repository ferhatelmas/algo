class FoxAndWord:
    def howManyPairs(self, words):
        def is_interesting(a, b):
            return any(a[i:] + a[:i] == b for i in xrange(len(a)))

        return sum(
            is_interesting(a, b) for i, a in enumerate(words) for b in words[i + 1 :]
        )
