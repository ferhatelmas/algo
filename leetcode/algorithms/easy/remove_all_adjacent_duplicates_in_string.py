class Solution:
    def removeDuplicates(self, S: str) -> str:
        res, l = [], 0
        for e in S:
            if l > 0 and res[l - 1] == e:
                res.pop()
                l -= 1
            else:
                res.append(e)
                l += 1
        return "".join(res)
