class BallAndHats:
    def getHat(self, hats, numSwaps):
        i = hats.index('o')
        if not numSwaps:
            return i
        elif i == 1:
            return 1 - numSwaps%2
        else:
            return self.getHat('.o.', numSwaps-1)
