class Cards:
    def deal(self, numPlayers, deck):
        res = map(
            lambda i: "".join(i),
            zip(
                *map(
                    lambda i: deck[i : i + numPlayers],
                    xrange(0, (len(deck) / numPlayers) * numPlayers, numPlayers),
                )
            ),
        )
        return res if res else [""] * numPlayers
