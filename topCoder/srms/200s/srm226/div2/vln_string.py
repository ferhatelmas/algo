class VLNString:
    def makeAcronym(self, longName):
        return ''.join(map(lambda w: w[0].upper(),
                           filter(lambda w: w not in ['and', 'the', 'of'],
                                  longName.split())))
