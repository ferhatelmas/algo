class EasyConversionMachine:
    def isItPossible(self, originalWord, finalWord, k):
        c = sum(i != j for i, j in zip(originalWord, finalWord))
        return  'IM' * (c > k or (k-c)%2) + 'POSSIBLE'
