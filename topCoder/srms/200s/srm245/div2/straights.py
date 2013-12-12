from operator import mul

class Straights:
    def howMany(self, hand, k):
        return sum(map(lambda i: reduce(mul, hand[i:i+k], 1),
                       xrange(len(hand)-k+1)))
