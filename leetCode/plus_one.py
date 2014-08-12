class Solution:
    def plusOne(self, digits):
        return [int(e) for e in str(int(''.join(str(e) for e in digits)) + 1)]
