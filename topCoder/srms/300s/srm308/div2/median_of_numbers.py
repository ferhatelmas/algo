class MedianOfNumbers:
    def findMedian(self, numbers):
        l = len(numbers)
        if l%2 == 0:
            return -1
        return sorted(numbers)[l/2]
