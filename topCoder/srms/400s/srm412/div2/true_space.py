from math import ceil

class TrueSpace:
    def calculateSpace(self, sizes, clusterSize):
        return sum(int(ceil(float(s) / clusterSize))*clusterSize for s in sizes)
