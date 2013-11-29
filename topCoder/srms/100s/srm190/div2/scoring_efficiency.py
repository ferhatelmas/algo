class ScoringEfficiency:
    def getPointsPerShot(self, gameLog):
        m1 = s1 = m2 = s2 = m3 = s3 = 0
        for l in gameLog:
            if l == "Made 2 point field goal":
                m2 += 1
                s2 += 1
            elif l == "Missed 2 point field goal":
                m2 += 1
            elif l == "Made 3 point field goal":
                m3 += 1
                s3 += 1
            elif l == "Missed 3 point field goal":
                m3 += 1
            elif l == "Made free throw":
                m1 += 1
                s1 += 1
            else:
                m1 += 1
        return (s1 + s2 * 2 + s3 * 3) / (m2 + m3 + 0.5 * m1)
