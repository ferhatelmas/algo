class CuttingPoles:
    def countCuts(self, poles):
        poles, c, avg = list(poles), 0, sum(poles) / len(poles)
        poles.sort()
        while poles[-1] > avg:
            c += 1
            poles[0], poles[-1] = poles[0] + poles[-1] - avg, avg
            poles.sort()
        return c
