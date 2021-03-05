class LuckyTicketSubstring:
    def maxLength(self, s):
        l = len(s)
        for i in xrange(l / 2, 0, -1):
            for j in xrange(l - 2 * i + 1):
                if sum(map(int, s[j : j + i])) == sum(map(int, s[j + i : j + 2 * i])):
                    return 2 * i
        return 0
