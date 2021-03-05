class SoccerLeagues:
    def points(self, matches):
        res = [0] * len(matches)
        for i, r in enumerate(matches):
            for j, c in enumerate(r):
                if c == "W":
                    res[i] += 3
                elif c == "D":
                    res[i] += 1
                    res[j] += 1
                elif c == "L":
                    res[j] += 3
        return res
