class Highscore:
    def getRank(self, scores, newscore, places):
        scores = sorted(list(scores) + [newscore], reverse=True)
        i, j = scores.index(newscore), len(scores) - scores[::-1].index(newscore)
        if j > places:
            return -1
        return i + 1
