class VerifyCreditCard:
    def checkDigits(self, cardNumber):
        l = len(cardNumber) % 2
        ls = [2 * int(e) if i % 2 == l else int(e) for i, e in enumerate(cardNumber)]
        return (
            "VALID"
            if sum(map(lambda e: sum(map(int, str(e))), ls)) % 10 == 0
            else "INVALID"
        )
