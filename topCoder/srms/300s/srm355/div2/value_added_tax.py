class ValueAddedTax:
    def calculateFinalPrice(self, product, price, food):
        if product in food:
            return price * 1.1
        return price * 1.18
