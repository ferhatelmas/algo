class ProgressBar:
    def showProgress(self, taskTimes, tasksCompleted):
        p, r = sum(taskTimes[:tasksCompleted]), sum(taskTimes[tasksCompleted:])
        n = (p * 20) / (p + r)
        return "#" * n + "." * (20 - n)
