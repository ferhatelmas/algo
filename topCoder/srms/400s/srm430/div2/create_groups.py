class CreateGroups:
    def minChanges(self, groups, minSize, maxSize):
        a, b, c, l = map(
            sum,
            zip(*((g, max(minSize - g, 0), max(g - maxSize, 0), 1) for g in groups)),
        )
        if a > maxSize * l or minSize * l > a:
            return -1
        return max(b, c)
