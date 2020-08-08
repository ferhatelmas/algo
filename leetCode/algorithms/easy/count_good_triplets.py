from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for i, x in enumerate(arr):
            for j, y in enumerate(arr[i + 1 :]):
                if abs(x - y) <= a:
                    for z in arr[i + j + 2 :]:
                        if abs(y - z) <= b and abs(x - z) <= c:
                            cnt += 1
        return cnt
