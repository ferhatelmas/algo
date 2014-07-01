class DivideByZero:
    def CountNumbers(self, numbers):
        s, g = set(), set(numbers)
        while len(g)-len(s):
            s, g = g, set()
            for i in s:
                g.add(i)
                for j in s:
                    g.add(j)
                    if i > j and j:
                        g.add(i / j)
                    elif j > i and i:
                        g.add(j / i)
        return len(g)
