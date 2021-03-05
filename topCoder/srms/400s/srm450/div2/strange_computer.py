from itertools import groupby


class StrangeComputer:
    def setMemory(self, mem):
        return sum(
            1
            for i, (k, _) in enumerate(groupby(mem))
            if k == "1" or (k == "0" and i > 0)
        )
