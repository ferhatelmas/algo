class TestCurve:
    def determineGrades(self, scores):
        m = max(scores)
        return map(lambda e: 100 * e / m, scores)
