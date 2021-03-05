class Rounder:
    def round(self, n, b):
        m = n % b
        return n - m if m < (b / 2 + b % 2) else n + b - m
