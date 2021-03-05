class CondorcetVoting:
    def winner(self, votes):
        l = len(votes[0])
        c = [[0] * l for _ in xrange(l)]
        for v in votes:
            for i in xrange(l):
                for j in xrange(l):
                    if v[i] < v[j]:
                        c[i][j] += 1
        for i in xrange(l):
            b = True
            for j in xrange(l):
                if i != j and c[i][j] <= c[j][i]:
                    b = False
            if b:
                return i
        return -1
