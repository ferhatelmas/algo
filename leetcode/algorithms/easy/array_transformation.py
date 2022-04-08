from typing import List


class Solution:
    def transform(self, arr: List[int]) -> List[int]:
        res, l = [], len(arr)
        for i, e in enumerate(arr):
            if i == 0 or i == l - 1:
                res.append(e)
            elif e > arr[i - 1] and e > arr[i + 1]:
                res.append(e - 1)
            elif e < arr[i - 1] and e < arr[i + 1]:
                res.append(e + 1)
            else:
                res.append(e)
        return res

    def transformArray(self, arr: List[int]) -> List[int]:
        n = self.transform(arr)
        while n != arr:
            n, arr = self.transform(n), n
        return n
