import bisect


class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        radius, l = 0, len(heaters)
        for h in houses:
            current = 10**9
            left = bisect.bisect_right(heaters, h)
            if left:
                current = min(current, h - heaters[left - 1])
            right = bisect.bisect_left(heaters, h)
            if right != l:
                current = min(current, heaters[right] - h)
            radius = max(radius, current)
        return radius
