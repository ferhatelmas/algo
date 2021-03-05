class SantaGifts:
    def distribute(self, gifts, N):
        s = [[] for _ in xrange(N)]
        for i, e in enumerate(gifts):
            if len(s[i % N]) < 4:
                s[i % N].append(e)
        return map(lambda ss: " ".join(ss), s)
