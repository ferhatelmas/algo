class ArrayHash:
    def getHash(self, input):
        return sum(
            map(
                lambda (j, s): sum(
                    map(lambda (i, e): ord(e) - ord("A") + i + j, enumerate(s))
                ),
                enumerate(input),
            )
        )
