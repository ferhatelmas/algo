import math

class RaceApproximator:
    def timeToBeat(self, d1, t1, d2, t2, raceDistance):
        t = t1*math.e**(math.log(float(t2)/t1)*math.log(float(d1)/raceDistance)/math.log(float(d1)/d2))
        return '%d:%02d:%02d' % (t/3600, (t%3600)/60, t%60)
