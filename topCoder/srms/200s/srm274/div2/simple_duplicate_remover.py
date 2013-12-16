class SimpleDuplicateRemover:
    def process(self, sequence):
        s, r = set(), []
        for e in sequence[::-1]:
            if e not in s:
                r.append(e)
                s.add(e)
        return r[::-1]
