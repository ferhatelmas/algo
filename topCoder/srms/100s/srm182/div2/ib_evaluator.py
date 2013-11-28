class IBEvaluator:
    def getSummary(self, predictedGrades, actualGrades):
        r, l = [0]*7, len(actualGrades)
        for p, a in zip(predictedGrades, actualGrades):
            r[abs(p-a)] += 1
        return map(lambda i: i*100/l, r)
