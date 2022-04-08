class Solution(object):
    def canMeasureWater(self, x, y, z):
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        return z == 0 or z <= x + y and z % gcd(x, y) == 0
