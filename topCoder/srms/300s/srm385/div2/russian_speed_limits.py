class RussianSpeedLimits:
    def getCurrentLimit(self, signs):
        c, s = True, 60
        for sign in signs:
            if sign == 'default':
                s = 60 if c else 90
            elif sign == 'city':
                s = 90 if c else 60
                c = not c
            else:
                s = int(sign)
        return s
