class TaxTable:
    def income(self, taxAmount):
        n = round((taxAmount + 6525) * 100.0 / 25)
        if 100000 <= n < 117250:
            return n
        n = round((taxAmount + 10042.5) * 100 / 28)
        if 117250 <= n < 178650:
            return n
        n = round((taxAmount + 18975) * 100.0 / 33)
        if 178650 <= n < 319100:
            return n
        n = round((taxAmount + 25357) * 100.0 / 35)
        if 319100 <= n:
            return n
        return -1
