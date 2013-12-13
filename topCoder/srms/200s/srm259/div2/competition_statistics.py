class CompetitionStatistics:
    def consecutiveGrowth(self, ratingChanges):
        c, m = 0, 0
        for r in ratingChanges:
            if r > 0:
                c += 1
            else:
                m = max(c, m)
                c = 0
        return max(c, m)
