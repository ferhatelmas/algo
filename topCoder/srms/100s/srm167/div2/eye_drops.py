class EyeDrops:
    def closest(self, sleepTime, k):
        if k == 1:
            return 1440.0
        k = float(k)
        if sleepTime < (24 - sleepTime) / (k - 1):
            return (24 / k) * 60
        return (24 - sleepTime) / (k - 1) * 60
