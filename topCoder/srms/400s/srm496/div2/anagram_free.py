class AnagramFree:
    def getMaximumSubset(self, S):
        return len(set(map(tuple, map(sorted, S))))
