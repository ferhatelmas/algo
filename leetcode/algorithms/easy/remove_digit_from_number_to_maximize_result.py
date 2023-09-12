class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ls = []
        for i, e in enumerate(number):
            if e == digit:
                ls.append(number[:i] + number[i + 1 :])
        return sorted(ls, reverse=True)[0]
