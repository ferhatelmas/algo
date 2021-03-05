class SumOfPower:
    def findSum(self, array):
        l = len(array)
        return sum(
            sum(array[j : j + i]) for i in xrange(1, l + 1) for j in xrange(l - i + 1)
        )
