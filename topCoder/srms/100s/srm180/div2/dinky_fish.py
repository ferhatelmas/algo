class DinkyFish:
    def monthsUntilCrowded(self, tankVolume, maleNum, femaleNum):
        m, s, i = min(maleNum, femaleNum), maleNum + femaleNum, 0
        while tankVolume * 2 >= s:
            m *= 2
            s += m
            i += 1
        return i
