class Solution:
    def numberToWords(self, num):
        below20 = ('One Two Three Four Five Six Seven Eight Nine Ten '
                   'Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen '
                   'Eighteen Nineteen').split()
        tens = ('x x Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'
                ).split()

        def words(n):
            if n < 20:
                return below20[n - 1:n]
            if n < 100:
                return [tens[n / 10]] + words(n % 10)
            if n < 1000:
                r, q = divmod(n, 100)
                return [below20[r - 1]] + ['Hundred'] + words(q)
            for w, p in zip(('Billion', 'Million', 'Thousand'), (3, 2, 1)):
                r, q = divmod(n, 1000**p)
                if r > 0:
                    return words(r) + [w] + words(q)

        return ' '.join(words(num)) or 'Zero'
