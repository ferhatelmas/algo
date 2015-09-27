class Solution:
    def diffWaysToCompute(self, ss):
        res = []
        for i, e in enumerate(ss):
            if e in '-+*':
                for a in self.diffWaysToCompute(ss[:i]):
                    for b in self.diffWaysToCompute(ss[i+1:]):
                        if e == '-':
                            res.append(a - b)
                        elif e == '+':
                            res.append(a + b)
                        else:
                            res.append(a * b)
        if not res:
            res.append(int(ss))
        return res
