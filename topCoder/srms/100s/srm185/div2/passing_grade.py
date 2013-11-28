from math import ceil

class PassingGrade:
    def pointsNeeded(self, pointsEarned, pointsPossible, finalExam):
        t = ceil((sum(pointsPossible) + finalExam) * 0.65 - sum(pointsEarned))
        return -1 if t > finalExam else max(0, t)
