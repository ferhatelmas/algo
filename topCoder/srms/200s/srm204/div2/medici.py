class Medici:
    def winner(self, fame, fortune, secrets):
        l = map(lambda p: min(p), zip(fame, fortune, secrets))
        m = max(l)
        if l.count(m) > 1:
            return -1
        return l.index(m)
