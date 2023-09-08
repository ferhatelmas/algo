class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        for i, w in enumerate(words[:-1]):
            if w[-1] != words[i + 1][0]:
                return False
        return words[0][0] == words[-1][-1]
