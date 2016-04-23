class Solution:
    vowels = "aeiouAEIOU"

    def reverseVowels(self, s):
        ls, j = list(s), len(s) - 1

        def f(start, end):
            while start > end and ls[start] not in self.vowels:
                start -= 1
            if ls[start] in self.vowels:
                return start
            return -1

        for i, e in enumerate(ls):
            if i >= j:
                break
            if e in self.vowels:
                j = f(j, i)
                if j == -1:
                    break
                else:
                    ls[i], ls[j] = ls[j], ls[i]
                j -= 1
        return "".join(ls)
