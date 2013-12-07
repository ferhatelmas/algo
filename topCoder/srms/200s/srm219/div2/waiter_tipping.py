class WaiterTipping:
    def maxPercent(self, total, taxPercent, money):
        r = money - total - total * taxPercent / 100
        if r < 0:
            return -1
        i = 1
        while True:
            if total * i / 100 > r:
                return i - 1
            i += 1
