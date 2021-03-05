class ContestCoordinator:
    def bestAverage(self, scores):
        l, scores = len(scores), sorted(scores)
        m = sum(scores) / float(l)
        for i in xrange(l / 2 + l % 2):
            m = max(m, sum(scores[i:-i]) / float(l - 2 * i))
        return m
