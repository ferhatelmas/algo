class Solution(object):
    def thirdMax(self, nums):
        n1 = n2 = n3 = None
        for e in nums:
            if e != n1 and e != n2 and e != n3:
                if n1 is None or e > n1:
                    n1, n2, n3 = e, n1, n2
                elif n2 is None or e > n2:
                    n2, n3 = e, n2
                elif n3 is None or e > n3:
                    n3 = e
        return n1 if n3 is None else n3
