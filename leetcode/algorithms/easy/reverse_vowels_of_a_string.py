class Solution:
    vowels = "aeiouAEIOU"

    def reverseVowels(self, s):
        vowels = [e for e in s if e in self.vowels]
        return "".join(vowels.pop() if e in self.vowels else e for e in s)
