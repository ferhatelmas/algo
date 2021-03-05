class MeasuringTemperature:
    def averageTemperature(self, measuredValues):
        ns, c = 0, 0
        for i, n in enumerate(measuredValues):
            if n >= -273:
                m = 1001
                for e in (
                    measuredValues[max(i - 2, 0) : i] + measuredValues[i + 1 : i + 3]
                ):
                    m = min(m, abs(n - e))
                print m
                if m < 3:
                    ns += n
                    c += 1
        return ns / float(c) if c else -300.0
