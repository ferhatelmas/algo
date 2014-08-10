class ExerciseMachine:
    def getPercentages(self, time):
        s = sum(map(lambda (a, b): a*b, zip((3600, 60, 1), map(int, time.split(':')))))
        return sum((s*i) % 100 == 0 for i in xrange(1, 100))
