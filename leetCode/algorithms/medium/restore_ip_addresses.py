class Solution:
    def restoreIpAddresses(self, s):
        self.ip = set()
        self.restore([], 0, s)
        return self.ip

    def restore(self, curr, o, s):
        if o >= 4:
            if not s and o == 4:
                self.ip.add(".".join(curr))
            return
        for i in range(1, 4):
            if s[:i] and int(s[:i]) < 256 and str(int(s[:i])) == s[:i]:
                self.restore(curr + [s[:i]], o + 1, s[i:])
            else:
                break
