from itertools import groupby

class FauxPalindromes:
    def classifyIt(self, word):
        if word == word[::-1]:
            return 'PALINDROME'
        else:
            s = ''.join(k for k, g in groupby(word))
            return 'FAUX' if s == s[::-1] else 'NOT EVEN FAUX'
