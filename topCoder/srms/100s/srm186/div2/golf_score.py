class GolfScore:
    def tally(self, parValues, scoreSheet):
        cp = {
            "triple bogey": 3,
            "double bogey": 2,
            "bogey"       : 1,
            "par"         : 0,
            "birdie"      : -1,
            "eagle"       : -2,
            "albatross"   : -3,
            "hole in one" : 1,
        }
        return sum(map(lambda (p, s): 1 if s == 'hole in one' else p+cp[s],
                       zip(parValues, scoreSheet)))
