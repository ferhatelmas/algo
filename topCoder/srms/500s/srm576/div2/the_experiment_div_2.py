class TheExperimentDiv2:
    def determineHumidity(self, intensity, L, leftEnd):
        blocked, ls = [False] * len(intensity), []
        for i in leftEnd:
            ls.append(
                sum(
                    ins
                    for ins, b in zip(intensity[i : i + L], blocked[i : i + L])
                    if not b
                )
            )
            for j in xrange(i, i + L):
                blocked[j] = True
        return ls
