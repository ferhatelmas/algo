class Solution:

    def canCompleteCircuit(self, gas, cost):
        tg = tc = md = d = s = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tg += g
            tc += c
            d = tg - tc
            if d < md:
                md, s = d, i
        return -1 if tc > tg else (s + 1) % len(gas)
