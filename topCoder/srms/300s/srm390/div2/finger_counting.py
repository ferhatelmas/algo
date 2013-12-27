class FingerCounting:
    def maxNumber(self, weakFinger, maxCount):
        c, i, f = 0, 1, True
        while True:
            if i == weakFinger:
                if maxCount == 0:
                    break
                maxCount -= 1
            c += 1
            i += 1 if f else -1
            if i in [1, 5]:
                f = not f
        return c
