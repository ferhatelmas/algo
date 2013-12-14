class GradingSystem:
    def fairness(self, scores, grades):
        s, hg = 0, 0
        for g in grades:
            hg = max(hg, g)
            s += hg
        hg = 8
        for g in grades[::-1]:
            hg = min(hg, g)
            s -= hg
        return s
