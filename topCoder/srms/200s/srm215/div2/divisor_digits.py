class DivisorDigits:
    def howMany(self, number):
        return len(filter(lambda i: i != '0' and number%int(i) == 0, str(number)))
