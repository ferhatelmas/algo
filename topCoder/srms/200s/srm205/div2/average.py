class Average:
    def belowAvg(self, math, verbal):
        avg = (sum(math) + sum(verbal)) / float(len(math))
        return len(filter(lambda (m, v): m + v < avg, zip(math, verbal)))
