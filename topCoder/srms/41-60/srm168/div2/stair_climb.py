from math import ceil

class StairClimb:
    def stridesTaken(self, flights, stairsPerStride):
        return int(reduce(lambda e, f: e + ceil(float(f)/stairsPerStride) + 2, flights, 0) - 2)
