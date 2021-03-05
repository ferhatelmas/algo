class CyclicWords:
    def differentCW(self, words):
        def get_canonical(s):
            if not s:
                return s
            return sorted([s[i:] + s[:i] for i in xrange(len(s))])[0]

        return len(set(get_canonical(w) for w in words))
