class Solution:
    def distMoney(self, money: int, children: int) -> int:
        received = 0
        if money < children:
            return -1
        if money > 8 * children:
            return children - 1
        while money > 0 and money - 8 >= children - 1:
            received += 1
            money -= 8
            children -= 1
        if money == 4 and children == 1:
            received -= 1
        return received
