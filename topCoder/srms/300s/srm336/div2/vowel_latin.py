class VowelLatin:
    def translate(self, word):
        v, a, b = "aeiou", "", ""
        for e in word:
            if e.lower() in v:
                b += e
            else:
                a += e
        return a + b
