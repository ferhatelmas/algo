from math import ceil

class RoomNumber:
    def numberOfSets(self, roomNumber):
        s = str(roomNumber)
        cs = [s.count(str(i)) for i in xrange(10) if i != 6 and i != 9]
        return max(int(ceil((s.count('6') + s.count('9')) / 2.0)), *cs)
