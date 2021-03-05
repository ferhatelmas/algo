class Truckloads:
    def numTrucks(self, numCrates, loadSize):
        if numCrates <= loadSize:
            return 1
        return self.numTrucks(numCrates / 2, loadSize) + self.numTrucks(
            (numCrates + 1) / 2, loadSize
        )
