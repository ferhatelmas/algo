class Solution:
    def digitSum(self, s: str, k: int) -> str:
        l = len(s)
        while l > k:
            n = []
            for i in range(0, l, k):
                n.append(str(sum(int(e) for e in s[i : i + k])))
            s = "".join(n)
            l = len(s)
        return s
