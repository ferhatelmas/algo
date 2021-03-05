class TournamentJudging:
    def getPoints(self, rawScores, conversionFactor):
        return sum(
            [int(round(float(r) / c)) for r, c in zip(rawScores, conversionFactor)]
        )
