class StringMult:
    def times(self, sFactor, iFactor):
        if sFactor == "" or iFactor == 0:
            return ""
        elif iFactor < 0:
            return sFactor[::-1] * abs(iFactor)
        return sFactor * iFactor
