class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        n, d = divmod(purchaseAmount, 10)
        if d >= 5:
            n += 1
        return 100 - 10 * n
