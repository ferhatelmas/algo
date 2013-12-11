from math import log
from operator import itemgetter

class ComputationalComplexity:
    def fastestAlgo(self, constant, power, logPower, N):
        return min(map(lambda (i, (c, p, l)): (i, c*N**p*log(N)**l),
                       enumerate(zip(constant, power, logPower))), key=itemgetter(1, 0))[0]
