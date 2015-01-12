class Solution:

    ns = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]

    def intToRoman(self, s):
        ls = []
        for i, c in self.ns:
            k = s / i
            ls.append(c * k)
            s -= k * i
        return (
            ''.join(ls)
            .replace('DCCCC', 'CM')
            .replace('CCCC', 'CD')
            .replace('LXXXX', 'XC')
            .replace('XXXX', 'XL')
            .replace('VIIII', 'IX')
            .replace('IIII', 'IV')
        )
