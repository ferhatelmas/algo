class AccountBalance:
    def processTransactions(self, startingBalance, transactions):
        for t in transactions:
            if t.startswith("C"):
                startingBalance += int(t.split()[1])
            else:
                startingBalance -= int(t.split()[1])
        return startingBalance
