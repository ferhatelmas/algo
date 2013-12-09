class NoisySensor:
    def medianFilter(self, data):
        r = [sorted(data[i-1:i+2])[1] for i in xrange(1, len(data)-1)]
        if r:
            return [data[0]] + r + [data[-1]]
        return data
