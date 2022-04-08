from itertools import izip_longest


class Solution(object):
    def addStrings(self, num1, num2):
        ls, carry = [], 0
        for a, b in izip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            carry, n = divmod(int(a) + int(b) + carry, 10)
            ls.append(str(n))
        if carry:
            ls.append(str(carry))
        return "".join(reversed(ls))
