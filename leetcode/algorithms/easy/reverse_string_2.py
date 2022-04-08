class Solution(object):
    def reverseStr(self, s, k):
        res = []
        for i in range(0, len(s), 2 * k):
            res.append(s[i : i + k][::-1])
            res.append(s[i + k : i + 2 * k])
        return "".join(res)
