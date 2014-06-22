from collections import Counter

class CheatingQuiz:
    def howMany(self, answers):
        c, r = Counter(answers), []
        for e in answers:
            r.append(sum(v > 0 for v in c.values()))
            c[e] -= 1
        return r
