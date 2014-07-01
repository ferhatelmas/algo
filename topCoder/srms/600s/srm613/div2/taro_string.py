class TaroString:
    def getAnswer(self, S):
        c = 'CAT'
        if not all(S.count(e) == 1 for e in c):
            return 'Impossible'
        for e in S:
            if c and e == c[0]:
                c = c[1:]
        return 'Impossible' if c else 'Possible'
