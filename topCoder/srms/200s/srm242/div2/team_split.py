class TeamSplit:
    def difference(self, strengths):
        strengths = sorted(list(strengths))
        return abs(sum(strengths[::2]) - sum(strengths[1::2]))
