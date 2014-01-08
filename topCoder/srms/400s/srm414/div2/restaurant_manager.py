from bisect import bisect_left, insort

class RestaurantManager:
    def allocateTables(self, tables, groupSizes, arrivals, departures):
        a, e, la, le, c = sorted(tables), [], len(tables), 0, 0
        for g, ar, dep in zip(groupSizes, arrivals, departures):
            i = 0
            while i < le and e[i][0] <= ar:
                insort(a, e.pop(i)[1])
                la, le = la+1, le-1

            i = bisect_left(a, g)
            if i < la:
                insort(e, (dep, a.pop(i)))
                la, le = la-1, le+1
            else:
                c += g
        return c
