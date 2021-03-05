class MountainWalk:
    def cellsVisited(self, areaMap, heightDifference):
        c, i, j, l1, l2 = 1, 0, 0, len(areaMap), len(areaMap[0])
        v, a = [[False] * l2 for _ in xrange(l1)], areaMap
        while True:
            v[i][j] = True
            if (
                i < l1 - 1
                and not v[i + 1][j]
                and abs(int(a[i + 1][j]) - int(a[i][j])) <= heightDifference
            ):
                i += 1
            elif (
                j > 0
                and not v[i][j - 1]
                and abs(int(a[i][j - 1]) - int(a[i][j])) <= heightDifference
            ):
                j -= 1
            elif (
                i > 0
                and not v[i - 1][j]
                and abs(int(a[i - 1][j]) - int(a[i][j])) <= heightDifference
            ):
                i -= 1
            elif (
                j < l2 - 1
                and not v[i][j + 1]
                and abs(int(a[i][j + 1]) - int(a[i][j])) <= heightDifference
            ):
                j += 1
            else:
                break
            c += 1
        return c
