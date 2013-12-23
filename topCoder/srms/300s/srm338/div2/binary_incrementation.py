class BinaryIncrementation:
    def plusOne(self, x):
        return bin(int(x, 2) + 1)[2:]
