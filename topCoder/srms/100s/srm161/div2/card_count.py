class CardCount:
    def dealHands(self, numPlayers, deck):
        n, r = len(deck) / numPlayers, [""] * numPlayers
        for i in xrange(n):
            for j in xrange(numPlayers):
                r[j] = r[j] + deck[numPlayers * i + j]
        return r
