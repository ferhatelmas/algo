class Solution(object):
    def fizzBuzz(self, n):
        def c(x):
            if x % 15 == 0:
                return "FizzBuzz"
            elif x % 3 == 0:
                return "Fizz"
            elif x % 5 == 0:
                return "Buzz"
            return str(x)

        return [c(x) for x in range(1, n + 1)]
