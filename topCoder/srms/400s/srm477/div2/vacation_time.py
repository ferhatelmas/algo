class VacationTime:
    def bestSchedule(self, N, K, workingDays):
        def c(i):
            return sum(map(lambda e: i <= e < i + K, workingDays))

        return min(c(i) for i in xrange(1, N - K + 2))
