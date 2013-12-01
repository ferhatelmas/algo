class Reppity:
    def longestRep(self, input):
        l = len(input)
        for i in xrange(l/2, 0, -1):
            for j in xrange(l-i+1):
                if input[j:i+j] in input[i+j:]:
                    return i
        return 0
