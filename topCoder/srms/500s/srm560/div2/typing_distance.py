class TypingDistance:
    def minDistance(self, keyboard, word):
        i, c = keyboard.index(word[0]), 0
        for e in word:
            j = keyboard.index(e)
            c += abs(i - j)
            i = j
        return c
