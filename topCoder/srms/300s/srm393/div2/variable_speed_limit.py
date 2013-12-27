class VariableSpeedLimit:
    def journeyTime(self, journeyLength, speedLimit):
        s, i, l = 0, 0, len(speedLimit)
        while journeyLength:
            if journeyLength <= speedLimit[i]:
                s += journeyLength / float(speedLimit[i])
                journeyLength = 0
            else:
                s += 1
                journeyLength -= speedLimit[i]
            i = (i+1)%l
        return s
