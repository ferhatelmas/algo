from itertools import permutations

class IrreducibleNumber:
    def getIrreducible(self, A):
        ns = set()
        for i in range(1, 4):
            for e in permutations(A, i):
                ns.add(sum(e))
        i = 1
        while i in ns:
            i += 1
        return i
