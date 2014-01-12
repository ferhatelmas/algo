class GymTraining:
    def trainingTime(self, needToTrain, minPulse, maxPulse, trainChange, restChange):
        p, c = minPulse, 0
        if maxPulse - minPulse >= trainChange:
            while needToTrain > 0:
                if p + trainChange <= maxPulse:
                    p += trainChange
                    needToTrain -= 1
                else:
                    p = max(minPulse, p-restChange)
                c += 1
        return -1 if needToTrain else c
