from operator import itemgetter


class CatchTheBeatEasy:
    def ableToCatchAll(self, x, y):
        t, xx = 0, 0
        for i, j in sorted(zip(x, y), key=itemgetter(1)):
            if abs(i - xx) > j - t:
                return "Not able to catch"
            else:
                xx = i
                t = j
        return "Able to catch"
