class ImportantTasks:
    def maximalCost(self, complexity, computers):
        co, cc = sorted(complexity, reverse=True), sorted(computers, reverse=True)
        lo, lc, i, j, c = len(co), len(cc), 0, 0, 0
        while i < lo and j < lc:
            if co[i] <= cc[j]:
                c += 1
                j += 1
            i += 1
        return c
