class Grader:
    def grade(self, predictedGrades, actualGrades):
        l = len(actualGrades)
        d = map(lambda (p, a): abs(p - a), zip(predictedGrades, actualGrades))
        return [d.count(i) * 100 / l for i in xrange(7)]
