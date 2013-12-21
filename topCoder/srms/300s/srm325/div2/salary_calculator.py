class SalaryCalculator:
    def calcHours(self, P1, P2, salary):
        base = P1 * 200
        if base >= salary:
            return float(salary) / P1
        return 200 + float(salary - base) / P2
