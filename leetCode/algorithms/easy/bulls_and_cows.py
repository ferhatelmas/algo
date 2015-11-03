from collections import Counter as c


class Solution:
    def getHint(self, secret, guess):
        bulls, diffa, diffb = 0, [], []
        for a, b in zip(secret, guess):
            if a == b:
                bulls += 1
            else:
                diffa.append(a)
                diffb.append(b)
        cows = sum(v for k, v in (c(diffa) & c(diffb)).items())
        return "{}A{}B".format(bulls, cows)
