class TheAirTripDivTwo:
    def find(self, flights, fuel):
        i, j = 0, len(flights)
        while fuel >= 0 and i < j and flights[i] <= fuel:
            fuel -= flights[i]
            i += 1
        return i
