class StreetParking:
    def freeParks(self, street):
        c, l = 0, len(street)
        for i in xrange(l):
            if (street[i] == '-' and
                'B' not in street[i+1:i+3] and
                'S' not in street[max(i-1, 0):i+2]):
                c += 1
        return c
