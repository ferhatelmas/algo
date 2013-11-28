class DiskSpace:
    def minDrives(self, used, total):
        u, c, t = sum(used), 0, sorted(list(total), reverse=True)
        while u > 0:
            u -= t[c]
            c += 1
        return c
