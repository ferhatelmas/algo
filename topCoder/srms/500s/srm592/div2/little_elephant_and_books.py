from sys import maxint


class LittleElephantAndBooks:
    def getNumber(self, pages, number):
        ls, l, m = sorted(pages), len(pages), maxint
        s = sum(ls[:number])
        for i in xrange(number):
            for j in xrange(number, l):
                m = min(m, s + ls[j] - ls[i])
        return m
