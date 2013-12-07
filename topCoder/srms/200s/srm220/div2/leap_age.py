class LeapAge:
    def getAge(self, year, born):
        def is_leap(y):
            return not (y%100 == 0 and y%400 != 0) and y%4 == 0
        return len(filter(is_leap, xrange(born+1, year+1)))
