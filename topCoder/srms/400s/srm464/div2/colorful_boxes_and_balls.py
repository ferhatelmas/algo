class ColorfulBoxesAndBalls:
    def getMaximum(self, numRed, numBlue, onlyRed, onlyBlue, bothColors):
        return max(
            (numRed - i) * onlyRed + (numBlue - i) * onlyBlue + 2 * i * bothColors
            for i in xrange(0, min(numRed, numBlue) + 1)
        )
